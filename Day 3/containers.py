class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

    def __str__(self):
        return f"cloud properties: {self.__tags}"


cloud = TagCloud()
cloud.add("density")
cloud.add("weight")
cloud.add("volume")
cloud.add("volume")
cloud.__setitem__("weight", 50)
print(cloud.tags["PYTHON"])
