class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = [end]
            else:
                self.graph_dict[start].append(end)

        print("Graph Dict: ", self.graph_dict)

    def get_paths(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return None

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths

    def shortest_path(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return -path
        if start not in self.graph_dict:
            return None
        shortest = None
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.shortest_path(node, end, path)
                if new_path:
                    if shortest is None or len(new_path) < len(shortest):
                       shortest = new_path
        return shortest

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Dubai", "New York"),
        ("Paris", "New York"),
        ("New York", "Toronto")
    ]
    start = "Mumbai"
    end = "New York"
    route_graph = Graph(routes)
    new_routes = route_graph.get_paths(start, end)
    print(new_routes)

    short_path = route_graph.shortest_path(start, end)
    print(short_path)
