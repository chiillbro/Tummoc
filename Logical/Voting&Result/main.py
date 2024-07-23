def vote(candidate_votes, name):
    if name in candidate_votes:
        candidate_votes[name] += 1
        return True
    else:
        return False

def print_winner(candidate_votes):
    max_votes = max(candidate_votes.values())
    winners = [name for name, votes in candidate_votes.items() if votes == max_votes]
    
    for winner in winners:
        print(winner)

def main():
    candidates = ["Alice", "Bob", "Charlie"] #Example list of candidates
    candidate_votes = {candidate: 0 for candidate in candidates}

    votes = ["Alice", "Bob", "Charlie", "Alice", "Alice", "Bob", "David"] #Example list of votes

    for name in votes:
        success = vote(candidate_votes, name)
        if not success:
            print(f"Invalid vote for {name}")

    print("Vote count:", {k: v for k, v in sorted(candidate_votes.items(), key=lambda item: item[1], reverse=True)})
    print("Winner(s):")
    print_winner(candidate_votes)

if __name__ == "__main__":
    main()
