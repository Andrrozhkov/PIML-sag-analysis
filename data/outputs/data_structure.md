
# Структура данных

## Формат хранения результатов
```python
# np-массив с структурой проводов
wire_data = np.array([
    (span_id, wire_id, a, b, c, x1, y1, z1, x2, y2, z2, sag, length, tension),
    ...
], dtype=structured_dtype)
```
