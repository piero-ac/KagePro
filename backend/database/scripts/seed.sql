-- Seed Data
INSERT INTO catalog (audio_id, title, language, duration, s3_key) VALUES
    ('a1b2c3d4-0001-0001-0001-000000000001', 'Genki Dialogue 1', 'japanese', 45, 'catalog/japanese/genki-dialogue-1.mp3'),
    ('a1b2c3d4-0001-0001-0001-000000000002', 'Genki Dialogue 2', 'japanese', 60, 'catalog/japanese/genki-dialogue-2.mp3'),
    ('a1b2c3d4-0001-0001-0001-000000000003', 'JLPT N2 Listening 1', 'japanese', 90, 'catalog/japanese/jlpt-n2-listening-1.mp3');

INSERT INTO session (session_id, user_id, language, date, duration, activity_type) VALUES
    ('b1b2c3d4-0002-0002-0002-000000000001', 'user_test_123', 'japanese', '2026-04-01 09:00:00', 45, 'shadowing'),
    ('b1b2c3d4-0002-0002-0002-000000000002', 'user_test_123', 'japanese', '2026-04-02 10:00:00', 30, 'listening'),
    ('b1b2c3d4-0002-0002-0002-000000000003', 'user_test_123', 'japanese', '2026-04-03 08:30:00', 20, 'reading'),
    ('b1b2c3d4-0002-0002-0002-000000000004', 'user_test_123', 'japanese', '2026-04-04 11:00:00', 60, 'shadowing');

INSERT INTO session_details (session_id, audio_id, user_audio_id, title, description) VALUES
    -- shadowing session with full details
    ('b1b2c3d4-0002-0002-0002-000000000001', 'a1b2c3d4-0001-0001-0001-000000000001', 'users/user_test_123/sessions/b1b2c3d4-0002-0002-0002-000000000001/attempt.mp3', 'Genki Dialogue 1 Attempt', 'First attempt, struggled with pitch accent'),
    -- listening session, no audio references
    ('b1b2c3d4-0002-0002-0002-000000000002', NULL, NULL, 'JLPT N2 Practice', 'Focused on listening comprehension'),
    -- reading session, no audio references
    ('b1b2c3d4-0002-0002-0002-000000000003', NULL, NULL, 'Yotsuba Chapter 3', 'Read slowly, looked up 10 words'),
    -- shadowing session with full details
    ('b1b2c3d4-0002-0002-0002-000000000004', 'a1b2c3d4-0001-0001-0001-000000000002', 'users/user_test_123/sessions/b1b2c3d4-0002-0002-0002-000000000004/attempt.mp3', 'Genki Dialogue 2 Attempt', 'Better rhythm this time, need to work on speed');