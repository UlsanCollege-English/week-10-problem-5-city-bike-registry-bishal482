[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/KIk995tI)
# HW05 — City Bike Registry (Resizing Chaining Map)

**Story intro (new theme):**  
A city runs a **bike share**. Each bike has an **ID**. You map **bike id → station**. As the fleet grows, the table must stay fast. Implement **auto-resize** when load is high.

**Today’s topic focus:** Chaining + **load factor** + **resize** (rehash).

---

## Technical description
- **Goal:** Implement a small **HashMap** that **resizes** (doubles bucket count) when `load factor > 0.75`.
- **Class to write in `main.py`:**
  - `class HashMap:` with:
    - `__init__(self, m=4)`
    - `put(self, key, value)`  # insert or overwrite
    - `get(self, key)` → value or `None`
    - `delete(self, key)` → True/False
    - `__len__(self)` → number of pairs
- **Behavior:** On insert, if `(len(self)+1)/bucket_count > 0.75`, **resize** and **rehash** all pairs.
- **Constraints:** Keys and values are strings. Only standard library.
- **Expected complexity:** Average **O(1)** for ops; resize is **O(n)** but rare (amortized O(1)).

---

## ESL scaffold — The 8 Steps
**Minimal prompts (hw05):**  
- **Read:** Keep map fast as size grows.  
- **Plan:** Check load; resize first; then insert.  
- **Students own all steps.**

---

## Hints
- Store buckets as `list` of lists of `[key, value]`.
- Write `_index(key, m)` and `_resize(new_m)` helpers.
- Reinsert pairs during resize (recompute index!).

---

## How to run tests locally
```
python -m pytest -q
```


---

## FAQ
**Q1. When to resize?** Before the insert that would push load over `0.75`.  
**Q2. Rehash?** Yes, compute new index with the **new** bucket count.  
**Q3. Delete?** Remove pair from its bucket; return True/False.  
**Q4. Complexity?** Amortized O(1); occasional O(n) during resize.  
**Q5. Mutate inputs?** Do not modify keys/values.  
**Q6. Grading?** Pytest autograder.  
**Q7. Order?** Any order is fine; not graded.