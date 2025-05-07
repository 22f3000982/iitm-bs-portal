BEGIN TRANSACTION;
CREATE TABLE assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            yt_link TEXT, watch_count INTEGER DEFAULT 0,
            FOREIGN KEY (course_id) REFERENCES courses(id)
        );
INSERT INTO "assignments" VALUES(1,1,'new c','https://youtu.be/VT9ToOPawW0',2);
INSERT INTO "assignments" VALUES(2,1,'sampledd','https://youtu.be/tnInGENQaVc',0);
INSERT INTO "assignments" VALUES(3,3,'MLF  End Term PYQ  | Jan 23 FN','https://youtu.be/4uUYBwIQMNg',0);
INSERT INTO "assignments" VALUES(4,3,'MLF  End Term PYQ  | May 23 FN','https://youtu.be/Bv4NA-TDdro',0);
INSERT INTO "assignments" VALUES(5,3,'MLF  End Term PYQ  | May 23 AN','https://youtu.be/oFShvOKqjxg',1);
INSERT INTO "assignments" VALUES(6,3,'MLF  End Term PYQ  | September 23 AN','https://youtu.be/QgxHiQQN4mU',0);
INSERT INTO "assignments" VALUES(7,3,'MLF  End Term PYQ  | Jan 24','https://youtu.be/8dj3sX5FYX8',0);
INSERT INTO "assignments" VALUES(8,3,'MLF  End Term PYQ  | May 24','https://youtu.be/KFx1nhlCSkg',0);
INSERT INTO "assignments" VALUES(9,3,'MLF  End Term PYQ  | September 24','https://youtu.be/YFejynQhdtY',0);
INSERT INTO "assignments" VALUES(10,3,'MLF  End Term PYQ  | Jan 25','',0);
INSERT INTO "assignments" VALUES(11,4,'MLT End Term PYQ | Jan 24','https://youtu.be/ucBQvcVu1II',0);
INSERT INTO "assignments" VALUES(12,5,'PDSA Week-9 PYQ','https://youtu.be/CR_GF9siGGc',0);
INSERT INTO "assignments" VALUES(13,5,'PDSA Week-11 PYQ','',0);
INSERT INTO "assignments" VALUES(14,5,'PDSA End Term PYQ | September 23 AN','https://youtu.be/q6cI-nvL9_w',1);
INSERT INTO "assignments" VALUES(15,5,'PDSA End Term PYQ | Jan 24 FN','https://youtu.be/bilgN4EdbLk',0);
INSERT INTO "assignments" VALUES(16,5,'PDSA OPPE PYQ Set-1','https://youtu.be/4AMkJ9mI-oI',0);
INSERT INTO "assignments" VALUES(17,5,'PDSA OPPE PYQ Set-2','https://youtu.be/U8jsBwhe3TI',0);
INSERT INTO "assignments" VALUES(18,9,'DBMS Week-9 One Shot Revision','https://youtu.be/easRDRwivTY',0);
INSERT INTO "assignments" VALUES(19,9,'DBMS Week-10 One Shot Revision Part-1','https://youtu.be/H2RFmItDEh0',0);
INSERT INTO "assignments" VALUES(20,9,'DBMS Week-10 One Shot Revision Part-2','https://youtu.be/XhQse4oZP-M',0);
INSERT INTO "assignments" VALUES(21,9,'DBMS Week-11 One Shot Revision ','https://youtu.be/oU8bDX5E0UQ',0);
INSERT INTO "assignments" VALUES(22,9,'DBMS Week-12 One Shot Revision Part-1','https://youtu.be/QHiqNebNP7s',0);
INSERT INTO "assignments" VALUES(23,9,'DBMS Week-12 One Shot Revision Part-2','https://youtu.be/Cy9LuqeBE1Y',0);
CREATE TABLE courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
INSERT INTO "courses" VALUES(1,'Business Analytics ');
INSERT INTO "courses" VALUES(3,'MLF');
INSERT INTO "courses" VALUES(4,'MLT');
INSERT INTO "courses" VALUES(5,'PDSA(Theory+OPPE)');
INSERT INTO "courses" VALUES(9,'DBMS (Theory+OPPE)');
CREATE TABLE notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            yt_link TEXT, watch_count INTEGER DEFAULT 0,
            FOREIGN KEY (course_id) REFERENCES courses(id)
        );
INSERT INTO "notes" VALUES(2,1,'sample c','https://youtu.be/1ecukKO2r5g',2);
INSERT INTO "notes" VALUES(3,3,'MLF Quiz-2 PYQ  | Jan 2023','https://youtu.be/t0zDodn69fk',0);
INSERT INTO "notes" VALUES(4,3,'MLF Quiz-2 PYQ  | May 2023','https://youtu.be/1aFlukVN9vM',0);
INSERT INTO "notes" VALUES(5,3,'MLF Quiz-2 PYQ  | September 2023','https://youtu.be/vaj4TkwDGCI',0);
INSERT INTO "notes" VALUES(6,3,'MLF Quiz-2 PYQ  | Jan 24','https://youtu.be/jcDcIrN5ED0',0);
INSERT INTO "notes" VALUES(7,3,'MLF Quiz-2 MOCK','https://youtu.be/bBNR_eYIWFc',0);
INSERT INTO "notes" VALUES(8,3,'MLF Quiz-2 PYQ  | May 24','https://youtu.be/GJYTP0Bb_fw',0);
INSERT INTO "notes" VALUES(9,3,'MLF Quiz-2 PYQ  | September 24','https://youtu.be/ZTbZbdCvO3U',0);
INSERT INTO "notes" VALUES(10,3,'MLF  Quiz-2 PYQ | Jan 25','',0);
INSERT INTO "notes" VALUES(11,4,'MLT QUIZ-2 MOCK','https://youtu.be/LXoNyBrrOAo',0);
INSERT INTO "notes" VALUES(12,4,'MLT Quiz-2 PYQ | Jan 24','https://youtu.be/PGXY0CwZeNQ',0);
INSERT INTO "notes" VALUES(13,4,'MLT Quiz-2 PYQ | May 24','https://youtu.be/NQgYjrFkXoo',0);
INSERT INTO "notes" VALUES(14,5,'PDSA Week-5 PYQ','https://youtu.be/TU8i3jICbZM',0);
INSERT INTO "notes" VALUES(15,5,'PDSA Week-6 PYQ','https://youtu.be/cNqMFB9Cm68',0);
INSERT INTO "notes" VALUES(16,5,'PDSA Week-7 PYQ','https://youtu.be/kJxAh7nYTak',0);
INSERT INTO "notes" VALUES(17,5,'PDSA Week-8 PYQ','https://youtu.be/CR_GF9siGGc',0);
INSERT INTO "notes" VALUES(18,5,'PDSA Quiz-2 PYQ | Jan 23','https://youtu.be/siGORn9MAug',0);
INSERT INTO "notes" VALUES(19,5,'PDSA Quiz-2 PYQ | September 23','https://youtu.be/QbewTYOpDTw',0);
INSERT INTO "notes" VALUES(20,9,'DBMS Week-5 One Shot Revision','https://youtu.be/MHN7HN8zQ28',0);
INSERT INTO "notes" VALUES(21,9,'DBMS Week-6 One Shot Revision','https://youtu.be/AG8w_J9vaTQ',0);
INSERT INTO "notes" VALUES(22,9,'DBMS Week-8 One Shot Revision Part-1','https://youtu.be/AG8w_J9vaTQ',0);
INSERT INTO "notes" VALUES(23,9,'DBMS Week-8 One Shot Revision Part-2','https://youtu.be/-MiPacTEjTE',0);
CREATE TABLE pyqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            yt_link TEXT, watch_count INTEGER DEFAULT 0,
            FOREIGN KEY (course_id) REFERENCES courses(id)
        );
INSERT INTO "pyqs" VALUES(2,1,'Course Intro Video','https://youtu.be/VT9ToOPawW0',1);
INSERT INTO "pyqs" VALUES(3,1,'Week-1 Theory + PA + Question','https://youtu.be/tnInGENQaVc',1);
INSERT INTO "pyqs" VALUES(4,1,'Week-2 Theory + PA + Question','https://youtu.be/ng7H0pz0ec0',2);
INSERT INTO "pyqs" VALUES(7,3,'MLF Week-2 Activity Question','https://youtu.be/8xPykL8_miI?si=ffcXp7gqzOQCzt5e',0);
INSERT INTO "pyqs" VALUES(8,9,'DBMS Week-1 One Shot Revision','https://youtu.be/xQfSvRzJOQ4',0);
INSERT INTO "pyqs" VALUES(9,9,'DBMS Week-2 One Shot Revision','https://youtu.be/8gCgg0KrRT8',0);
INSERT INTO "pyqs" VALUES(10,3,'MLF Week-3 Activity Question','https://youtu.be/5iRjPm39TR0',0);
INSERT INTO "pyqs" VALUES(11,3,'MLF Week-4 Activity Question','https://youtu.be/o9Ifuw-NmaA',0);
INSERT INTO "pyqs" VALUES(12,3,'MLF  Quiz-1 PYQ | September 23','https://youtu.be/ApaNZzRQZMY',0);
INSERT INTO "pyqs" VALUES(13,3,'MLF  Quiz-1 PYQ | Jan 24','https://youtu.be/93bOUjx-bJo',0);
INSERT INTO "pyqs" VALUES(14,3,'MLF  Quiz-1 PYQ | May 24','https://youtu.be/NNbusI2kv-4',0);
INSERT INTO "pyqs" VALUES(15,3,'MLF  Quiz-1 PYQ | September 24','https://youtu.be/FpMJ5I948pI',0);
INSERT INTO "pyqs" VALUES(16,3,'MLF  Quiz-1 PYQ | Jan 25','',0);
INSERT INTO "pyqs" VALUES(17,4,'MLT Week-1 Activity Question','https://youtu.be/LD3FhSg9Shk',0);
INSERT INTO "pyqs" VALUES(18,4,'MLT Week-2 Activity Question','https://youtu.be/tmdC-E58x9w',0);
INSERT INTO "pyqs" VALUES(19,4,'MLT Week-3 Activity Question','https://youtu.be/_LUB8dQxMMU',0);
INSERT INTO "pyqs" VALUES(20,4,'MLT QUIZ-1 MOCK','https://youtu.be/pe8AtHjR6w4',0);
INSERT INTO "pyqs" VALUES(21,4,'MLT Quiz-1 PYQ | May 23','https://youtu.be/ZAIl_SHFEhI',0);
INSERT INTO "pyqs" VALUES(22,4,'MLT Quiz-1 PYQ | September 23','https://youtu.be/9wkVlD6pWQs',0);
INSERT INTO "pyqs" VALUES(23,4,'MLT Quiz-1 PYQ | Jan 24','https://youtu.be/n_ulXMBwNhU',0);
INSERT INTO "pyqs" VALUES(24,4,'MLT Quiz-1 PYQ | September 24','https://youtu.be/G07lrcEo5T8',0);
INSERT INTO "pyqs" VALUES(26,5,'PDSA Week-2 PYQ','https://youtu.be/7E4yPHHyOYA',0);
INSERT INTO "pyqs" VALUES(27,5,'PDSA Week-3 PYQ','https://youtu.be/4iNU_E2_y9k',0);
INSERT INTO "pyqs" VALUES(28,5,'PDSA Week-4 PYQ','https://youtu.be/V2RZ8PY37Ts',0);
INSERT INTO "pyqs" VALUES(29,5,'PDSA Quiz-1 PYQ | Jan 24','https://youtu.be/FNfmEJqK8bU',0);
INSERT INTO "pyqs" VALUES(30,5,'PDSA Quiz-1 PYQ | May 24','https://youtu.be/MGchbfQqXt4',0);
INSERT INTO "pyqs" VALUES(32,9,'DBMS OPPE PYQ PlayList','https://www.youtube.com/playlist?list=PLTewhG5vbW7EKmyl32LAzSJLcEtuK1fer',0);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('courses',12);
INSERT INTO "sqlite_sequence" VALUES('pyqs',32);
INSERT INTO "sqlite_sequence" VALUES('notes',24);
INSERT INTO "sqlite_sequence" VALUES('assignments',24);
COMMIT;
