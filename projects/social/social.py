import random
from util import Stack, Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # could create a list with all possible friendships combos
        friendships = []
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, num_users):
                friendships.append((user, friend))

        # shuffle the list,
        # random.shuffle(array)

        # Fisher-Yates shuffle
        for idx in range(len(friendships)):
            rand_idx = random.randint(0, len(friendships) - 1)
            friendships[idx], friendships[rand_idx] = friendships[rand_idx], friendships[idx]

        # then grab the first N elemts from the list.
        total_friendships = num_users * avg_friendships
        # add_friendship makes 2 friendships at a time
        pairs_needed = total_friendships // 2

        random_friendships = friendships[:pairs_needed]

        # Create friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # use BFT

        q = Queue()
        q.enqueue([user_id])
        visited = {}  # Note that this is a dictionary, not a set

        while q.size() > 0:
            path = q.dequeue()
            curr_id = path[-1]
            if curr_id not in visited:
                visited[curr_id] = path
                for id_friend in self.friendships[curr_id]:
                    copy_of_path = path.copy()
                    copy_of_path.append(id_friend)
                    q.enqueue(copy_of_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f'result of populating graph with friends: {sg.friendships}')
    connections = sg.get_all_social_paths(1)
    print(f'result of finding people in extended network: {connections}')
