# Applebaum-Arkis
An implementation of the secret sharing protocols described in Applebaum and Arkis' paper, "Conditional Disclosure of Secrets and d-Uniform Secret Sharing with Constant Information Rate" (2017). 
Lemma 4.2: Currently implemented using Shamir's secret sharing and Beimel-Peter's CDS protocols (3-party and odd-k), but can be tweaked to work with any SS and CDS (as long as the relevant function names match or are imported as such).

Requires: 
1. Python 3.6+
2. halp (http://murali-group.github.io/halp/)

TODO:
1. Add documentation
2. Implement Secret Sharing for even values of d
