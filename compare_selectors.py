import re


def compare_selectors(x, y):
    # Split the selectors into their components
    x_components = x.split()
    y_components = y.split()

    # Initialize variables to store the results
    same_chain = []
    forkpoint = None
    deviated_chain1 = []
    deviated_chain2 = []

    # Compare the components
    for i in range(min(len(x_components), len(y_components))):
        if x_components[i] == y_components[i]:
            same_chain.append(x_components[i])
        else:
            forkpoint = i
            break

    # If the selectors are identical up to the end of the shorter one
    if forkpoint is None:
        forkpoint = min(len(x_components), len(y_components))

    # Collect the deviated chains
    deviated_chain1 = x_components[forkpoint:]
    deviated_chain2 = y_components[forkpoint:]

    return {
        'forkpoint': forkpoint,
        'same_chain': ' '.join(same_chain),
        'deviated_chain1': ' '.join(deviated_chain1),
        'deviated_chain2': ' '.join(deviated_chain2)
    }
