__project__ = "Basic Webcrawler"

import os

# Each website crawled is separate project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("creating new directory")
        os.makedirs(directory)

def create_data_files(project_name, base_url):
    # create directory if does not exist
    create_project_dir(project_name)
    # save everything to that directory
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"

    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")

def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data + "\n")

def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + "\n")

def delete_file_content(path):
    with open(path, "w"):
        pass

# read file to set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# save the sets to file
def set_to_file(links, file_name):
    delete_file_content(file_name)
    for link in sorted(links):
        append_to_file(file_name, link)