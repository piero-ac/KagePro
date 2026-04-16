# KagePro

A Japanese language immersion tracker and shadowing app. Log study sessions, track streaks, and practice shadowing with reference audio clips.

---

## Tech Stack

- **Backend** — Python / FastAPI
- **Frontend** — React Native (Expo)
- **Auth** — Clerk
- **Database** — PostgreSQL (AWS RDS)
- **Storage** — AWS S3
- **Hosting** — AWS (EC2 or Elastic Beanstalk)

---

## API

### v1 — Session Logging ✅

Core activity logging for any immersion activity.

#### Sessions

| Method   | Endpoint                 | Description      |
| -------- | ------------------------ | ---------------- |
| `GET`    | `/sessions/{session_id}` | Get a session    |
| `POST`   | `/sessions`              | Create a session |
| `DELETE` | `/sessions/{session_id}` | Delete a session |

#### Session Details

| Method | Endpoint                         | Description                  |
| ------ | -------------------------------- | ---------------------------- |
| `GET`  | `/sessions/{session_id}/details` | Get session details          |
| `POST` | `/sessions/{session_id}/details` | Create session details       |
| `PUT`  | `/sessions/{session_id}/details` | Update title and description |

#### Stats

| Method | Endpoint | Description                                       |
| ------ | -------- | ------------------------------------------------- |
| `GET`  | `/stats` | Current streak, total time, breakdown by activity |

#### Supported Activity Types

- `shadowing`
- `listening`
- `reading`
- `writing`
- `online_tutoring`

---

### v2 — Audio & Shadowing 🚧 In Progress

Adds reference audio catalog and user recording uploads via S3 presigned URLs.

#### Catalog

| Method | Endpoint              | Description                                |
| ------ | --------------------- | ------------------------------------------ |
| `GET`  | `/catalog`            | List all reference audio clips             |
| `GET`  | `/catalog/{audio_id}` | Get clip metadata and presigned stream URL |

#### User Audio

| Method   | Endpoint              | Description                                |
| -------- | --------------------- | ------------------------------------------ |
| `GET`    | `/audio/{session_id}` | Get presigned URL for a recorded attempt   |
| `POST`   | `/audio/{session_id}` | Get presigned upload URL for a new attempt |
| `DELETE` | `/audio/{session_id}` | Delete a recording from S3                 |

---

## Database Schema

```sql
catalog         -- reference audio clip metadata + S3 keys
session         -- core activity log (language, date, duration, activity type)
session_details -- optional media references and notes per session
```

`session_details` cascades on session delete. `audio_id` sets null if a catalog entry is removed.

---

## Roadmap

- **v1** — Session logging + `/stats` ✅
- **v2** — S3 audio uploads for user recordings 🚧
- **v2.5** — Reference audio + shadowing upload comparison
- **v3** — Full shadowing comparison and scoring
