window.DATA = {
  member: { name: "Mei" },
  companion: { name: "Pip" },
  trip: { route: "HKG → Tokyo", label: "Mei's first flight to Tokyo" },
  miles: { before: 1250, missionReward: 50, after: 1300, annualCap: 2000 },
  missions: [
    { id: "checkin",  title: "Check-in Champion", reward: 30, status: "done" },
    { id: "boarding", title: "Boarding Badge",    reward: 50, status: "ready" },
    { id: "window",   title: "Window Watcher",    reward: 30, status: "locked" },
    { id: "arrival",  title: "Arrival Explorer",  reward: 40, status: "locked" }
  ],
  stamps: [
    { city: "Taipei",  collected: true },
    { city: "Bangkok", collected: true },
    { city: "Osaka",   collected: true },
    { city: "Tokyo",   collected: false }
  ],
  story: { title: "Mei and Pip Fly to Tokyo", text: "Today is a big day: Mei is flying to Tokyo for the very first time! Her paper-plane friend Pip is coming too, tucked safely in her backpack. Pip can't wait to peek out the window at the fluffy clouds below. Together they buckle up, smile big, and get ready for an adventure in the sky." },
  notifications: {
    linkRemoved: { title: "Cathay", body: "Your guardian link has been removed." },
    graduation:  { title: "Cathay", body: "Happy 18th, Mei! 🎓 Your miles, your history and 3 years of family transfers are coming with you." },
    future: [
      "Age 19: Family transfer received. Flying home for the holidays.",
      "Age 22: Graduation trip booked.",
      "Age 30: New junior member added: your daughter."
    ]
  },
  texts: {
    sweep:  [{ from: "Dad", body: "Moved your miles to my account last night before the cut-off 👍 Optimising." }],
    ending: [{ from: "Dad", body: "Can I borrow some miles?" }, { from: "Mei", body: "Optimising, Dad." }]
  },
  labels: {
    concept: "Concept screen · synthetic data",
    juniorMode: "Junior mode",
    milesOf: "of",
    milesThisYear: "miles this year",
    tripStory: "My trip story",
    missionsTitle: "Trip missions",
    stampsTitle: "My stamps",
    start: "Start",
    milesUnit: "miles"
  }
};
