
text = 'There are two different ways for rsync to contact a remote system: using a  remote-shell program as the transport (such as ssh or rsh) or contacting an rsync daemon directly via TCP.  The remote-shell transport is used whenever the source or destination path contains a single colon (:) separator after a  host  specification.   Contacting  an rsync daemon directly happens when the source or destination path contains a double colon (::) separator after a host specification, OR when an  rsync://  URL  is specified  (see  also  the "USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION" section for an exception to this latter rule).'
text = ' '.join(text.split())

def left_align(text, width):
    lines = []
    words = text.split(' ')
    inx = 0
    acc = []
    for word in words:
        if inx + len(word) + 1 >= width:
            lines.append(acc)
            inx = 0
            acc = []
        inx += len(word) + 1
        acc.append(word)
    return lines


print('x' * 40)
left_aligned = left_align(text, 40)
# print(left_aligned)
for line in left_aligned:
    print(' '.join(line))


def length_of_line(line):
    acc = 0
    for word in line[:-1]:
        acc += len(word) + 1
    acc += len(line[-1])
    return acc


def justify(lines, width):
    for line in lines:
        extra_spaces = width - length_of_line(line)
        spaces = list(' ' * extra_spaces)
        inx = 0
        while spaces:
            if inx >= len(line) - 1:
                inx = 0
            space = spaces.pop()
            line[inx] += space
            inx += 1
    return lines

print('')
print('x' * 40)
justified = justify(left_aligned, 40)
for line in justified:
    print(' '.join(line))
