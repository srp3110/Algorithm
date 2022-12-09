def ft_please(z):
    M = float(z)*0.3048
    return M

z = input("Convert ft to m >>")
M = ft_please(z)

print(z,"ft is", M, "m")