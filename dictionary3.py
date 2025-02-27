def main():
    a=dict(x='1',y=2,z=3)
    for k,v in a.items():
        print(f"{k}-{v}")

    for k in a.keys():
        print(k)

    for v in a.values():
        print('x' in a)
        print('Found!' if 'y' in a else 'y is not present in a')
        print('Found!' if 'd' in a else 'd is not present in a')
        print(a['x'])

if __name__=='__main__':main()
