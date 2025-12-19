import sqlite3
from ..config import Config
from .logger import logger

class DatabaseManager:
    def __init__(self):
        self.db_path = Config.DB_PATH
        self.init_db()

    def get_connection(self):
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row  # Access columns by name
            return conn
        except sqlite3.Error as e:
            logger.error(f"Database connection failed: {e}")
            return None

    def init_db(self):
        """Initialize the database with required tables."""
        conn = self.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                
                # Tasks Table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        status TEXT DEFAULT 'Pending' CHECK(status IN ('Pending', 'Done')),
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)

                # Notes Table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS notes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        content TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)

                # Expenses Table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        amount REAL NOT NULL,
                        category TEXT,
                        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                
                conn.commit()
                logger.info("Database initialized successfully.")
            except sqlite3.Error as e:
                logger.error(f"Error initializing database: {e}")
            finally:
                conn.close()

    def execute_query(self, query, params=()):
        """Execute a query (INSERT, UPDATE, DELETE)."""
        conn = self.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                return cursor.lastrowid
            except sqlite3.Error as e:
                logger.error(f"Query execution failed: {e}")
                return None
            finally:
                conn.close()

    def fetch_all(self, query, params=()):
        """Fetch all results for a SELECT query."""
        conn = self.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, params)
                return [dict(row) for row in cursor.fetchall()]
            except sqlite3.Error as e:
                logger.error(f"Fetch failed: {e}")
                return []
            finally:
                conn.close()

db = DatabaseManager()
