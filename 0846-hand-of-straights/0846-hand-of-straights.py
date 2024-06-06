class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()  # Sort the hand to make it easier to form consecutive groups
        hand_counts = {}  # Dictionary to store the count of each card
        
        # Count the occurrences of each card
        for card in hand:
            if card in hand_counts:
                hand_counts[card] += 1
            else:
                hand_counts[card] = 1
        
        for card in hand:
            if hand_counts[card] > 0:
                # Try to form a group starting from this card
                for i in range(card, card + groupSize):
                    if i not in hand_counts or hand_counts[i] == 0:
                        return False
                    hand_counts[i] -= 1
        
        return True
