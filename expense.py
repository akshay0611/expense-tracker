"""
Expense class - Represents a single expense entry
"""

from datetime import datetime
import uuid


class Expense:
    """Class representing a single expense"""
    
    def __init__(self, description, amount, category, date=None, expense_id=None):
        self.id = expense_id or str(uuid.uuid4())[:8]
        self.description = description
        self.amount = float(amount)
        self.category = category
        self.date = date or datetime.now().strftime("%Y-%m-%d")
    
    def to_dict(self):
        """Convert expense to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'description': self.description,
            'amount': self.amount,
            'category': self.category,
            'date': self.date
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create Expense object from dictionary"""
        return cls(
            description=data['description'],
            amount=data['amount'],
            category=data['category'],
            date=data['date'],
            expense_id=data['id']
        )
    
    def __str__(self):
        """String representation of expense"""
        return f"{self.id:<8} {self.date:<12} {self.description:<20} {self.category:<15} ${self.amount:>9.2f}"
    
    def __repr__(self):
        return f"Expense(id={self.id}, desc={self.description}, amount={self.amount}, category={self.category})"
