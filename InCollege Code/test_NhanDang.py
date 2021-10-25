import pytest
import friends
import sqlite3
import jobs

#function ro test whether remove friend function works
def test_removeFriend():
    friends.removeFriend("nhandang", "test")
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = ("SELECT FROM friends WHERE userName  = ? AND friend = ?")
    data=("nhandang", "test")
    assert c.execute(query, data) == ""

#function to check user friendlist initiated empty
def test_initialFriendList():
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = ("SELECT FROM friends WHERE userName  = ? ")
    data=("nhandang")
    assert c.execute(query, data) == ""

#function to test user can see all list jobs and description
def test_listJob():
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    jobs.postJob("asds", "adsd")
    assert jobs.getAllJobTitles() == c.execute("SELECT id, title FROM Jobs").fetchall()
    assert jobs.getJobDetails(1) == c.execute("SELECT * FROM Jobs WHERE id = ?", [1]).fetchone()

#function to test user can filter to see job have not applied
def test_filterNotAppliedJob():
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    assert jobs.getAllJobTitlesAppliedFor == c.execute("SELECT j.id, j.title FROM Jobs j INNER JOIN app_status a ON j.id = a.jobID WHERE status == 'applied' AND a.username = ?").fetchall()

#function to test for check delete job
def test_deleteJob():
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    assert jobs.getAllJobTitlesAppliedFor == c.execute("SELECT * FROM app_status WHERE username = ? AND status = 'deleted").fetchall()