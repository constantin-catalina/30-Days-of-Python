import csv

def main():

    lines_containing_python = 0
    lines_containing_javascript = 0
    lines_containing_java_not_javascript = 0

    with open('data/hacker_news.csv', 'r', encoding='utf-8') as file:
        data = csv.reader(file, delimiter=',')
        for row in data:
            row_text = ' '.join(row)
            if 'python' in row_text or 'Python' in row_text:
                lines_containing_python += 1
            if 'javascript' in row_text or 'JavaScript' in row_text or 'Javascript' in row_text:
                lines_containing_javascript += 1
            if 'Java' in row_text and not ('JavaScript' in row_text):
                lines_containing_java_not_javascript += 1
        
    print(f"Number of lines containing 'python' or 'Python': {lines_containing_python}")
    print(f"Number of lines containing 'JavaScript', 'javascript' or 'Javascript': {lines_containing_javascript}")
    print(f"Number of lines containing 'Java' and not 'JavaScript': {lines_containing_java_not_javascript}")

main() 