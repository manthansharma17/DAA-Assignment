# DAA Lab Task 1

This repository contains solutions for Part 1, Part 2, and Part 4 of DAA Lab Task 1.

---

## Part 1. Trace It Yourself

### Input

`8, 3, 15, 6, 2`

### Output

Largest number: `15`

Sorted list: `2, 3, 6, 8, 15`

### Comparisons Made

`4`

### Dry Run

| i | A[i] | Maximum | Comparisons |
|---|------|---------|-------------|
| 1 | 3 | 8 | 1 |
| 2 | 15 | 15 | 2 |
| 3 | 6 | 15 | 3 |
| 4 | 2 | 15 | 4 |

The first element, `8`, is considered the initial maximum. Each remaining element is compared with the current maximum.

### Sorting Method Used

**Selection Sort**

### Sorting Steps

Initial list:

`8, 3, 15, 6, 2`

After selecting the smallest elements step by step:

`2, 3, 15, 6, 8`

`2, 3, 6, 15, 8`

`2, 3, 6, 8, 15`

Final sorted list:

`2, 3, 6, 8, 15`

### Explanation

To find the maximum, the program starts with the first value and compares it with every remaining element. For `n` elements, this requires `n - 1` comparisons, so the maximum-finding process grows linearly with the input size.

Selection Sort repeatedly finds the smallest value from the unsorted portion and moves it to its correct position.

### Data Structure Used

A **list** is used to store the numbers.

### Complexity

- Finding maximum: `O(n)`
- Selection Sort: `O(n²)`

---

## Part 2. Stack or Queue

### Input

`Task1, Task2, Task3, Task4, Task5`

### Stack Order

A stack follows **LIFO (Last In, First Out)**.

`Task5 → Task4 → Task3 → Task2 → Task1`

### Queue Order

A queue follows **FIFO (First In, First Out)**.

`Task1 → Task2 → Task3 → Task4 → Task5`

### Printer Should Use

**Queue**

### Reason

A printer processes jobs in the same order in which they arrive. A queue guarantees this behavior because the first task added is also the first task removed for processing.

### Dry Run

**Stack (LIFO):**

Push:

`Task1 → Task2 → Task3 → Task4 → Task5`

Pop:

`Task5 → Task4 → Task3 → Task2 → Task1`

**Queue (FIFO):**

Enqueue:

`Task1 → Task2 → Task3 → Task4 → Task5`

Dequeue:

`Task1 → Task2 → Task3 → Task4 → Task5`

### Data Structures Used

- **Stack** for LIFO processing
- **Queue** for FIFO processing

### Complexity

Processing all `n` tasks requires `O(n)` time.

---

## Part 4. Count the Steps

### Single Loop

For:

```text
FOR i = 1 to 5
    PRINT i
```

The loop runs **5 times**.

### For n = 20

If the loop runs from `1` to `n` and `n = 20`, it runs:

**20 times**

### Nested Loop

For:

```text
FOR i = 1 to 5
    FOR j = 1 to 5
        PRINT i, j
```

The outer loop runs 5 times and the inner loop runs 5 times for every outer iteration.

Total PRINT executions:

`5 × 5 = 25`

**Nested loop total prints: 25**

### Dry Run

```text
i = 1 → inner loop runs 5 times
i = 2 → inner loop runs 5 times
i = 3 → inner loop runs 5 times
i = 4 → inner loop runs 5 times
i = 5 → inner loop runs 5 times

Total = 5 × 5 = 25
```

### For n = 10

Single loop:

`10` executions

Nested loop:

`10 × 10 = 100` executions

### Explanation

A single loop executes once for each input element, so its running time grows linearly as `O(n)`. A nested loop executes the inner operation `n` times for each of the `n` outer iterations, giving `n²` operations and `O(n²)` complexity.

### Data Structure Used

No special data structure is required for this part.

---

## Input Growth Analysis

If the input size becomes **100 times larger**:

For a linear `O(n)` algorithm, the work becomes approximately **100 times larger**.

For a quadratic `O(n²)` algorithm:

`100² = 10,000`

So the work becomes approximately **10,000 times larger**.

Therefore, maximum finding, task processing, and single loops grow **proportionally**, while Selection Sort and nested loops grow much more rapidly.

---

## How to Run

```bash
python part1_trace.py
python part2_stack_queue.py
python part4_complexity.py
```