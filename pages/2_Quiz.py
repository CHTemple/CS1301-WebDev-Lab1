import streamlit as st

st.title("How Well Do You Know Chess?")
st.write("Answer five questions to test your basic chess knowledge.")
st.image("Images/chess.jpg", width=300)

score = 0

answer1 = st.radio(
    "1. How many squares are on a standard chessboard?",
    [32, 48, 64, 100],
    index=None,
)  #NEW

if answer1 == 64:
    score += 1

answer2 = st.multiselect(
    "2. Which chess pieces can jump over other pieces?",
    ["Knight", "Bishop", "Rook", "Queen"]
)  #NEW

if answer2 == ["Knight"]:
    score += 1

st.image("Images/pawn.jpg", width=300)
answer3 = st.number_input(
    "3. How many pawns does each player begin with?",
    min_value=0,
    max_value=16,
    step=1
)  #NEW

if answer3 == 8:
    score += 1

answer4 = st.selectbox(
    "4. Which piece is generally considered to be worth about 9 points?",
    ["Pawn", "Bishop", "Rook", "Queen"],
    index=None
)

if answer4 == "Queen":
    score += 1

answer5 = st.radio(
    "5. What does checkmate mean?",
    [
        "The king has been captured",
        "The king is in check and has no legal escape",
        "A player has lost their queen",
        "Neither player can make a legal move"
    ],
    index=None
)

if answer5 == "The king is in check and has no legal escape":
    score += 1

st.image("Images/chessclock.jpg", width=300)
if st.button("See My Result"):
    st.write(f"Your score is {score} out of 5.")

    if score == 5:
        st.image("Images/brilliant.jpg", width=150)
        st.write("Brilliant! You are ready to beat Magnus Carlsen.")

    elif score >= 3:
        st.image("Images/inaccuracy.jpg", width=150)
        st.write("Inaccuracy! You have some understanding, but there's room for improvement.")

    else:
        st.image("Images/blunder.jpg", width=150)
        st.write("Blunder! Keep practicing to improve your chess skills.")