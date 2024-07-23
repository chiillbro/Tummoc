SELECT 
    t.station_id,
    s.name AS station_name,
    t.slot,
    t.time
FROM 
    times t
JOIN 
    station s ON t.station_id = s.id
WHERE 
    (t.station_id, t.slot, t.time) IN (
        SELECT
            station_id,
            slot,
            MIN(time)
        FROM 
            times
        GROUP BY 
            station_id, slot
    )
ORDER BY 
    t.station_id, t.slot, t.time;
