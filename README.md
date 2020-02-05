# countrytagger





## SQL commands

```sql
SELECT norm, COUNT(*) FROM places GROUP BY norm ORDER BY COUNT(*) DESC LIMIT 30;
```

```sql
SELECT norm, COUNT(DISTINCT country) FROM places GROUP BY norm HAVING COUNT(DISTINCT country) > 1;
```

```sql
SELECT norm, COUNT(DISTINCT country) FROM places GROUP BY norm ORDER BY COUNT(DISTINCT country) DESC LIMIT 30;
```