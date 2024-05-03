class Seat:
    def __init__(self, seat_id, row, column, status='available'):
        self.seat_id = seat_id
        self.row = row
        self.column = column
        self.status = status

class SeatingPlan:
    def __init__(self, seating_plan_id):
        self.seating_plan_id = seating_plan_id
        self.seats = []

    def add_seat(self, seat_id, row, column):
        seat = Seat(seat_id, row, column)
        self.seats.append(seat)

    def get_seat(self, seat_id):
        for seat in self.seats:
            if seat.seat_id == seat_id:
                return seat
        return None

    def update_seat(self, seat_id, status):
        seat = self.get_seat(seat_id)
        if seat:
            seat.status = status
        else:
            raise ValueError("Seat not found in the seating plan")
    
    def delete_seat(self, seat_id):
        for seat in self.seats:
            if seat.seat_id == seat_id:
                self.seats.remove(seat)
                return
        raise ValueError("Seat not found in the seating plan")

class Stadium:
    def __init__(self):
        self.seating_plans = {}

    def add_seating_plan(self, seating_plan_id):
        if seating_plan_id not in self.seating_plans:
            self.seating_plans[seating_plan_id] = SeatingPlan(seating_plan_id)
        else:
            raise ValueError("Seating plan ID already exists")

    def get_seating_plan(self, seating_plan_id):
        return self.seating_plans.get(seating_plan_id, None)

import unittest

class TestStadiumSeatingManagement(unittest.TestCase):
    def setUp(self):
        self.stadium = Stadium()
        self.stadium.add_seating_plan(1)
        self.seating_plan = self.stadium.get_seating_plan(1)
        self.seating_plan.add_seat(1, 1, 1)
        self.seating_plan.add_seat(2, 1, 2)

    def test_add_seat(self):
        self.assertEqual(len(self.seating_plan.seats), 2)

    def test_get_seat(self):
        seat = self.seating_plan.get_seat(1)
        #self.assertIsNotNone(seat)
        self.assertEqual(seat.seat_id, 1)

    def test_update_seat(self):
        self.seating_plan.update_seat(1, 'booked')
        seat = self.seating_plan.get_seat(1)
        self.assertEqual(seat.status, 'booked')
        
    def test_delete_seat(self):
        self.seating_plan.delete_seat(1)
        self.assertEqual(len(self.seating_plan.seats), 1)
        #self.assertIsNone(self.seating_plan.get_seat(1))


''' def test_add_existing_seating_plan(self):
        with self.assertRaises(ValueError):
            self.stadium.add_seating_plan(1)

    def test_get_nonexistent_seating_plan(self):
        seating_plan = self.stadium.get_seating_plan(2)
        self.assertIsNone(seating_plan)'''

if __name__ == '__main__':
    unittest.main(verbosity=5)
