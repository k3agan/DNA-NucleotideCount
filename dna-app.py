import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Page title

# image = Image.open('dna-logo.jpg')

# st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count

This app counts the nucleotide composition of DNA

***
""")

st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area('Sequence input', sequence_input, height = 250)
sequence = st.text_area('Sequence Input', sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]  # skips the sequence name (first line)
sequence = ''.join(sequence)  # concats list to string

st.write("""
***
""")

# print the input dna sequence
st.header('INPUT (DNA Query)')
sequence

# Dna nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

# print dictionary

st.subheader('1. Print dictionary')


def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d


X = DNA_nucleotide_count(sequence)

X


# 2. Print text
st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

# display dataframe

st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)


# display bar chart using altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # width of bar
)
st.write(p)
