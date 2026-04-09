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
    audio_id VARCHAR(50),
    user_audio_id VARCHAR(50),
    title VARCHAR(100),
    description VARCHAR(300),
    session_id UUID REFERENCES session(session_id)
);