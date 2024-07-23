SELECT 
    rp1.route_id,
    rp1.stop_id AS source_stop_id,
    rp2.stop_id AS dest_stop_id
FROM 
    route_points rp1
JOIN 
    route_points rp2 ON rp1.route_id = rp2.route_id AND rp1.order < rp2.order
WHERE 
    rp1.order = 1;
