SELECT 
    t.station_id,
    t.slot,
    t.time
FROM 
    times t
WHERE 
    t.station_id = @station_id AND t.slot = @slot;
