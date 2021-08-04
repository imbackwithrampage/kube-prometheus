from os import listdir, path


def get_crd_filenames():
    crd_dir = path.join('manifests', 'setup')
    crd_files = listdir(crd_dir)
    return [path.join(crd_dir, filename) for filename in crd_files]


def remove_crd_status(filename):
    with open(filename, 'r') as f:
        data = f.read()

    out_lines = []

    for line in data.splitlines():
        if line.startswith('status:'):
            break

        out_lines.append(line)

    out_lines.append('')

    with open(filename, 'w') as f:
        f.write('\n'.join(out_lines))


if __name__ == '__main__':
    for filename in get_crd_filenames():
        remove_crd_status(filename)
        print(f'Rewritten: {filename}')
