/* Shared content layer (Playbook §6): every concept renders this same object.
   All wording is lifted from thewealthtableglobal.com (see docs/SITE_EXTRACTION.md). */
window.WT = {
  name: 'The Wealth Table',
  tagline: 'Leave richer than you arrived.',
  email: 'info@thewealthtableglobal.com',
  phone: '+234 8096000049',
  address: '10, Onisiwo Road, Ikoyi, Lagos',
  social: {
    linkedin: 'https://ng.linkedin.com/in/udomaryanneokonjo',
    instagram: 'https://www.instagram.com/udo_okonjo'
  },
  rcc: 'https://rcc.africa/',
  img: (n) => 'img/photos/' + n + '.jpg',
  logo: (k, tone) => 'img/logo/' + k + '-' + (tone || 'cream') + '.png',

  gives: [
    'Invitations are released in waves, to the list before anyone else.',
    'The founding rate, held for you.',
    'Members of The Wealth Table are invited first.'
  ],
  pillars: ['Connection', 'Opportunity', 'Collaboration'],

  lagos: {
    city: 'Lagos', country: 'Nigeria',
    title: 'The Wealth Table™ Lagos',
    date: 'Sat, Nov 21st, 2026', dateShort: '21 Nov 2026',
    time: '11:00 AM – 5:00 PM (WAT)',
    venue: 'Civic Centre, VI Lagos',
    kicker: 'From Conversation to Action.',
    body: 'Building on the powerful conversations in Nairobi and Accra, The Wealth Table arrives in Lagos for a bold new chapter. This invitation-only gathering will bring together an exceptional circle of women leaders, entrepreneurs, investors, and wealth builders to explore one defining question:',
    question: 'How do we move more women from success to ownership?',
    fee: { rcc: '$200', non: '$300' },
    card: 'lagos-card', poster: 'lagos-event-poster'
  },

  nairobi: {
    city: 'Nairobi', country: 'Kenya', flag: '🇰🇪',
    venue: 'Kwetu Nairobi, Kenya',
    date: '13 June 2026',
    title: 'Nairobi – Where It All Began.',
    body: [
      'The inaugural edition of The Wealth Table brought together 24 remarkable women in Nairobi for an intimate, invitation-only gathering centred on wealth, ownership, opportunity and intentional connection.',
      'In a room defined by openness, generosity and bold conversations, women shared experiences, challenged assumptions and explored what it truly means to build and own wealth on their own terms.',
      'The word of the day was Courage, a fitting beginning to a growing global conversation about women, wealth and ownership.'
    ],
    women: '24', card: 'nairobi-card',
    cta: 'Join Next Nairobi Wait List',
    gallery: ['nairobi-10844','nairobi-10840','nairobi-10832','nairobi-10836','nairobi-10860','nairobi-10874','nairobi-10820','nairobi-10827','nairobi-10887','nairobi-10816','nairobi-10880','nairobi-10890','nairobi-10857','nairobi-10817','nairobi-10863']
  },

  accra: {
    city: 'Accra', country: 'Ghana', flag: '🇬🇭',
    venue: 'Cantonments, Accra, Ghana',
    date: '3 October 2026',
    title: 'Accra – Where It Continued.',
    body: [
      'Following its inaugural gathering in Nairobi, The Wealth Table arrived in Accra, bringing together approximately 25 remarkable women for an intimate, invitation-only evening of meaningful conversations and connections.',
      'Hosted in a beautiful private residence, the gathering created space for honest reflections on wealth, ownership, opportunity, and the power of women coming together with intention.',
      'The evening was marked by openness, shared wisdom, fresh perspectives, and a collective desire to move beyond conversations towards meaningful action.'
    ],
    closing: 'Different women. Shared ambition. Bigger possibilities.',
    women: '25', card: 'accra-card',
    cta: 'Join Next Accra Waitlist',
    gallery: ['accra-6762','accra-6797','accra-6949','accra-6679','accra-6923','accra-6917','accra-6585','accra-6582','accra-6618','accra-6912','accra-6565','accra-6812','accra-6823','accra-6626','accra-6725']
  },

  founder: {
    name: 'Udo Okonjo', first: 'Udo', last: 'Okonjo',
    role: 'Founder, Radiant Collective Capital',
    photo: 'founder-udo-okonjo',
    body: [
      'Udo Okonjo believes the next chapter of women’s success must be about more than achievement. It must be about ownership.',
      'An entrepreneur, investor, board director, and founder of Radiant Collective Capital, Udo has spent decades championing women’s leadership, economic advancement, and the power of building wealth with intention.',
      'She created The Wealth Table from a simple conviction: when accomplished women come together for honest conversations about money, power, opportunity and ownership, extraordinary possibilities emerge.',
      'More than another networking event, The Wealth Table is a space for meaningful connections, shared intelligence, bold thinking, and the conversations that inspire women to make bigger moves.'
    ],
    invitation: 'Her invitation is simple: Come to the table. Leave richer than you arrived.'
  },

  faq: [
    ['What is The Wealth Table?', 'The Wealth Table is a purposefully designed gathering where women connect around real opportunities, shared ambitions, and the future of wealth and ownership. It’s a place to bring what you’re building, explore what’s next, and connect with women whose knowledge, experience, relationships, and resources can open new possibilities. From business opportunities and investments to strategic partnerships and valuable introductions, The Wealth Table creates the environment for connections to become meaningful action.'],
    ['Who is The Wealth Table for?', 'The Wealth Table is for women who are building, investing, leading, creating and ready to make their next significant move. Whether you’re an entrepreneur exploring expansion, a professional building wealth, an investor seeking new perspectives or a leader looking to turn influence into ownership, there is a place for you at the table.'],
    ['Do I need to be a member of Radiant Collective Capital to attend?', 'No. The Wealth Table welcomes both RCC members and non-members. RCC members enjoy preferential participation rates.'],
    ['What can I expect at a gathering?', 'Expect an immersive experience built around meaningful connections, practical insights and real opportunities. Come prepared to share what you’re working on, the opportunities you’re exploring, the challenges you’re navigating and the kind of connections that could help you move forward. You may discover a potential collaborator, gain valuable investment intelligence, make an important introduction or uncover an opportunity you hadn’t previously considered. Rather than conventional conference presentations or sales pitches, the focus is on participation, contribution and making things happen.'],
    ['Is there a participation fee?', 'Yes. Participation fees vary by city and gathering. For The Wealth Table Lagos, participation is $200 for RCC members and $300 for non-members. Both rates provide access to the same premium gathering and experience.'],
    ['How do I register for The Wealth Table Lagos?', 'Click “Register for Lagos,” complete the registration form, select your applicable participation rate, and proceed to payment. Your registration will be confirmed following successful payment, subject to availability.'],
    ['When and where is The Wealth Table Lagos?', 'Saturday, 21 November 2026, at the Civic Centre, Victoria Island, Lagos, from 11:00 AM to 5:00 PM (WAT).'],
    ['Will The Wealth Table take place in other cities?', 'Yes. Following our inaugural gathering in Nairobi and our second gathering in Accra, The Wealth Table continues to expand across Africa and beyond, creating new spaces for women to connect, collaborate and unlock opportunities.'],
    ['How can I pay for my participation?', 'Participation fees are listed in US dollars, with the option to pay in Nigerian naira at the applicable local rate. Secure online payment options and the applicable amounts will be displayed during registration. Your participation will be confirmed once payment has been successfully completed.']
  ],

  closing: {
    head: 'Join us, we are about to do it again.',
    body: 'Together, we are redefining what financial empowerment looks like, creating a future where women lead with confidence, own assets with purpose, and build legacies that inspire generations to come.',
    cta: 'Join Our Future Waitlist Now'
  },
  footerLine: 'This is where women bring more than their stories to the table. They bring the businesses they’re building, the investments they’re exploring, the opportunities they’re pursuing, and the connections they need to make their next move.',
  consent: 'By subscribing, you agree to our Privacy Policy and provide consent to receive important updates from thewealthtableglobal.com. You can unsubscribe anytime.',
  tables: ['Lagos – Wealth Table', 'Accra – Wealth Table', 'Nairobi – Wealth Table', 'General – Wealth Table']
};
