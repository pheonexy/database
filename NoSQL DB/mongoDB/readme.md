# MongoDB Setup on Windows 10 (32-bit)

This repository documents my experience setting up MongoDB on a Windows 10 32‑bit machine, including challenges and solutions.
## ⚙️ Structure 
```
mongodb-setup-experience/
│
├── README.md                   # Project overview, setup steps, 
│
├── scripts/                    # Windows batch scripts
│   ├── start1_mongo.bat        # Start MongoDB server
│   ├── stop_mongo.bat          # Stop MongoDB service
|   └── start2_mongo.bat        # start mongodb using cfg
│
├── python/                     # queries & connector
│   ├── connect.py              # PyMongo connection script
│   ├── insert_one.py 
│   ├── insert_many.py 
│   └── select_query.py  
│
├── config/
│   ├── setup.md                # MongoDB configuration files
│   └── mongod.cfg              # Config with mmapv1 engine
│
├── data/                       # Placeholder for datasets
│    └── sample.json
│
└── Review.md                   # Lessons learned, difficulties


