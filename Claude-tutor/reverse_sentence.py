class SentenceReverser:
    """Process sentence reversal, maintaining word internal order"""
    
    def reverse_sentence(self, sentence: str) -> str:
        """
        Reverse the order of words in a sentence, keeping each word's internal letter order unchanged.
        
        Args:
            sentence: Input sentence with words separated by spaces
            
        Returns:
            str: Sentence with word order reversed
        """
        # Split sentence into list of words
        words = sentence.split()
        
        # Reverse word list
        words.reverse()
        
        # Join words with space
        return ' '.join(words)


def main():
    sentence = input().strip()
    
    reverser = SentenceReverser()
    result = reverser.reverse_sentence(sentence)
    
    print(result)


if __name__ == "__main__":
    main() 