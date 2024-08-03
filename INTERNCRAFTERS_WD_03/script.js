const boardElement = document.getElementById('board');
const statusElement = document.getElementById('status');
const resetButton = document.getElementById('reset');
const cells = document.querySelectorAll('.cell');
let board = ['', '', '', '', '', '', '', '', ''];
let currentPlayer = 'X';
let gameActive = true;

const winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

function handleCellClick(event) {
    const cell = event.target;
    const cellIndex = parseInt(cell.getAttribute('data-index'));

    if (board[cellIndex] !== '' || !gameActive) {
return;
    }

    updateCell(cell, cellIndex);
    checkResult();
}

function updateCell(cell, index) {
    board[index] = currentPlayer;
    cell.textContent = currentPlayer;
}

function checkResult() {
    let roundWon = false;

    for (let i = 0; i < winningConditions.length; i++) {
const [a, b, c] = winningConditions[i];
if (board[a] === '' || board[b] === '' || board[c] === '') {
    continue;
}
if (board[a] === board[b] && board[b] === board[c]) {
    roundWon = true;
    break;
}
    }

    if (roundWon) {
statusElement.textContent = `Player ${currentPlayer} wins!`;
gameActive = false;
return;
    }

    const roundDraw = !board.includes('');
    if (roundDraw) {
statusElement.textContent = `Draw!`;
gameActive = false;
return;
    }

    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    statusElement.textContent = `Player ${currentPlayer}'s turn`;
}

function resetGame() {
    board = ['', '', '', '', '', '', '', '', ''];
    gameActive = true;
    currentPlayer = 'X';
    statusElement.textContent = `Player X's turn`;
    cells.forEach(cell => cell.textContent = '');
}

cells.forEach(cell => cell.addEventListener('click', handleCellClick));
resetButton.addEventListener('click', resetGame);
