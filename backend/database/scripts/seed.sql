
INSERT INTO session (session_id, user_id, language, date, duration, activity_type) VALUES
    (gen_random_uuid(), 'user_test_123', 'ja', '2024-01-01 09:00:00', 30, 'shadowing'),
    (gen_random_uuid(), 'user_test_123', 'ja', '2024-01-02 09:00:00', 45, 'listening'),
    (gen_random_uuid(), 'user_test_123', 'es', '2024-01-03 09:00:00', 20, 'reading'),
    (gen_random_uuid(), 'user_test_123', 'ja', '2024-01-04 09:00:00', 60, 'shadowing');

INSERT INTO session_details (session_details_id, audio_id, user_audio_id, title, description, session_id)
SELECT
    gen_random_uuid(),
    'ja_news_clip_001',
    'user_attempt_001',
    'NHK News Clip 1',
    'Shadowed NHK morning news segment',
    session_id FROM session WHERE activity_type = 'shadowing' LIMIT 1;

INSERT INTO session_details (session_details_id, audio_id, title, description, session_id)
SELECT
    gen_random_uuid(),
    'ja_podcast_001',
    NULL,
    'Nihongo con Teppei Episode 312',
    session_id FROM session WHERE activity_type = 'listening' LIMIT 1;