import unicodecsv

enrollments_filename = 'enrollments.csv'

## Longer version of code (replaced with shorter, equivalent version below)

# enrollments = []
# f = open(enrollments_filename, 'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
#     enrollments.append(row)
# f.close()

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv(enrollments_filename)
    
### Write code similar to the above to load the engagement
### and submission data. The data is stored in files with
### the given filenames. Then print the first row of each
### table to make sure that your code works. You can use the
### "Test Run" button to see the output of your code.

engagement_filename = 'daily_engagement.csv'
submissions_filename = 'project_submissions.csv'
    
daily_engagement = read_csv(engagement_filename)     # Replace this with your code
project_submissions = read_csv(submissions_filename)  # Replace this with your code

print enrollments[0]
print daily_engagement[0]
print project_submissions[0]
