from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Genre, Base, Artist, User

engine = create_engine('sqlite:///musicv1.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Create dummy user
User1 = User(name="DB Created", email="dbCreated@yahoo.com")
session.add(User1)
session.commit()


genre1 = Genre(user_id=1, name="Alternative Rock")
session.add(genre1)
session.commit()

artist1 = Artist(user_id=1, name="Panic at the Disco", bio="Panic! at the Disco is an American rock band from Las Vegas, Nevada, formed in 2004 and featuring the current lineup of vocalist Brendon Urie, accompanied on tour by guitarist Kenneth Harris, drummer Dan Pawlovich, and bassist Nicole Row. Founded by Founded by childhood friends Ryan Ross, Spencer Smith, Brent Wilson and Urie, Panic! at the Disco recorded its first demos while its members were in high school.",
                     genre=genre1)
session.add(artist1)
session.commit()

artist2 = Artist(user_id=1, name="Fallout Boy", bio="Fall Out Boy is an American rock band formed in Wilmette, Illinois, a suburb of Chicago, in 2001. The band consists of lead vocalist and rhythm guitarist Patrick Stump, bassist Pete Wentz, lead guitarist Joe Trohman, and drummer Andy Hurley. The band originated from Chicago's hardcore punk scene, with which all members were involved at one point. The group was formed by Wentz and Trohman as a pop punk side project of the members' respective hardcore bands, and Stump joined shortly thereafter.",
                     genre=genre1)
session.add(artist2)
session.commit()

artist3 = Artist(user_id=1, name="Paramore", bio="Paramore is an American rock band from Franklin, Tennessee, formed in 2004. The band currently consists of lead vocalist Hayley Williams, guitarist Taylor York and drummer Zac Farro. Williams and Farro are founding members of the group, while York, a high school friend of the original lineup, joined in 2007. Williams is the only member to appear on all five of Paramore's studio albums and has been the only constant member of the band",
                     genre=genre1)
session.add(artist3)
session.commit()


genre2 = Genre(user_id=1, name="Jazz")
session.add(genre1)
session.commit()

artist1 = Artist(user_id=1, name="Nat King Cole", bio="Nathaniel Adams Coles March 17, 1919 to February 15, 1965, known professionally as Nat King Cole, was an American jazz pianist and vocalist. He recorded over one hundred songs that became hits on the pop charts. His trio was the model for small jazz ensembles that followed. Cole also acted in films and on television",
                     genre=genre2)
session.add(artist1)
session.commit()

artist2 = Artist(user_id=1, name="Leslie Odom Jr", bio="Leslie Odom Jr. born August 6, 1981 is an American actor and singer. He has performed on Broadway and in television and film, and has released two solo jazz albums. He is known for originating the role of Aaron Burr in the Broadway musical Hamilton, a performance for which he won the 2016 Tony Award for Best Actor in a Musical and the Grammy Award for Best Musical Theater Album as a principal vocalist. His television roles included Sam Strickland in the musical series Smash 2012 to 2013. He is also the author of the forthcoming 2018 book Failing Up.",
                     genre=genre2)
session.add(artist2)
session.commit()

artist3 = Artist(user_id=1, name="Kristofer Maddigan", bio="Kristofer Maddigan is a percussionist, drummer and composer based in Toronto, Canada. A member of the National Ballet of Canada Orchestra since 2010, Kris also performs regularly with a wide range of groups including The Toronto Symphony Orchestra, Hannaford Street Silver Band, The Canadian Opera Company, The Toronto Concert Orchestra, The Thunder-Bay Symphony, A Fantastica Batteria, and the Devah Quartet. Kris also works with numerous jazz, theatre and new music groups around the city.",
                     genre=genre2)
session.add(artist3)
session.commit()


genre3 = Genre(user_id=1, name="Classical")
session.add(genre3)
session.commit()

artist1 = Artist(user_id=1, name="Tchaikovskiy", bio="Pyotr Ilyich Tchaikovsky 25 May  1840 to 6 November 1893,was a Russian composer of the romantic period, some of whose works are among the most popular music in the classical repertoire. He was the first Russian composer whose music made a lasting impression internationally, bolstered by his appearances as a guest conductor in Europe and the United States. Tchaikovsky was honored in 1884 by Emperor Alexander III, and awarded a lifetime pension.",
                     genre=genre3)
session.add(artist1)
session.commit()

artist2 = Artist(user_id=1, name="Beethoven", bio="Ludwig van Beethoven was a German composer and pianist. A crucial figure in the transition between the Classical and Romantic eras in Classical music, he remains one of the most famous and influential of all composers. His best-known compositions include 9 symphonies, 5 piano concertos, 1 violin concerto, 32 piano sonatas, 16 string quartets, his great Mass the Missa solemnis, and one opera, Fidelio.",
                     genre=genre3)
session.add(artist2)
session.commit()

artist3 = Artist(user_id=1, name="Mozart", bio="Born in Salzburg, Mozart showed prodigious ability from his earliest childhood. Already competent on keyboard and violin, he composed from the age of five and performed before European royalty. At 17, Mozart was engaged as a musician at the Salzburg court, but grew restless and traveled in search of a better position. While visiting Vienna in 1781, he was dismissed from his Salzburg position. He chose to stay in the capital, where he achieved fame but little financial security. During his final years in Vienna, he composed many of his best-known symphonies, concertos, and operas, and portions of the Requiem, which was largely unfinished at the time of his early death at the age of 35. The circumstances of his early death have been much mythologized.",
                     genre=genre3)
session.add(artist3)
session.commit()

genre4 = Genre(user_id=1, name="Hip Hop")
session.add(genre4)
session.commit()

artist1 = Artist(user_id=1, name="Kendrick Lamar", bio="Kendrick Lamar Duckworth (born June 17, 1987) is an American rapper and songwriter. Raised in Compton, California, Lamar embarked on his musical career as a teenager under the stage name K-Dot, releasing a mixtape that garnered local attention and led to his signing with indie record label Top Dawg Entertainment (TDE).He began to gain recognition in 2010, after his first retail release, Overly Dedicated. The following year, he independently released his first studio album, Section.80, which included his debut single, \"HiiiPoWeR\". By that time, he had amassed a large online following and collaborated with several prominent artists in the hip hop industry, including The Game, Busta Rhymes, and Snoop Dogg.",
                     genre=genre4)
session.add(artist1)
session.commit()

artist2 = Artist(user_id=1, name="Drake", bio="Canadian rapper, singer, songwriter, record producer, actor, and entrepreneur.  Drake initially gained recognition as an actor on the teen drama television series Degrassi: The Next Generation in the early 00s. Intent on pursuing a career as a rapper, he departed the series in 2007 following the release of his debut mixtape, Room for Improvement. He released 2 further independent projects, Comeback Season and So Far Gone, before signing to Lil Wayne's Young Money Entertainment in June 2009",
                     genre=genre4)
session.add(artist2)
session.commit()

artist3 = Artist(user_id=1, name="Domo Genesis", bio="Dominique Marquis Cole (born March 9, 1991), known professionally as Domo Genesis, is an American rapper and disc jockey (DJ) from Los Angeles, California. He currently signed to Columbia Records and Odd Future Records. Aside from his solo career, Cole is a member of the alternative hip hop collective Odd Future and its subgroup MellowHigh. His debut solo studio album Genesis was released in March 2016.",
                     genre=genre4)
session.add(artist3)
session.commit()


print "added items!"
