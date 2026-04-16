DROP TABLE IF EXISTS session_details;
DROP TABLE IF EXISTS session;
DROP TABLE IF EXISTS catalog;

CREATE TABLE catalog (
    audio_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(100) NOT NULL,
    language VARCHAR(20) NOT NULL,
    duration INT,
    s3_key VARCHAR(255) NOT NULL
);

CREATE TABLE session (
    session_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id VARCHAR NOT NULL,
    language VARCHAR(20),
    date TIMESTAMP,
    duration INT,
    activity_type VARCHAR(20)
);

CREATE TABLE session_details (
    session_details_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES session(session_id) ON DELETE CASCADE,
    audio_id UUID REFERENCES catalog(audio_id) ON DELETE SET NULL,
    user_audio_id VARCHAR(255),
    title VARCHAR(100),
    description VARCHAR(300)
);