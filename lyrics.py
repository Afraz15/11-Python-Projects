love = "\nI been tryna call  I been on my own for long enough   Maybe you can show me how to love, maybe I'm going through withdrawals  You don't even have to do too much  You can turn me on with just a touch, baby\n"
driver = "\nI got my drivers license last week,  Just like we always talked about Cause you were so excited for me, To finally drive up to your house\n"
mood = "\nWhy you always in a mood? actin' brand new  I ain't tryna tell you what to do, but try to play it cool  Baby, I ain't playing by your rules  Everything look better with a view\n"
Time = "\nStop the clocks, it's amazing  You should see the way the light dances off your hair  A million colours of hazel, golden, and red  Saturday morning is fading  The sun's reflected by the coffee in your hand  My eyes are caught in your gaze all over again\n"

arr = [love, driver, mood, Time]

print(' 0. Love \n 1. Driver \n 2. Mood \n 3. Time \n')
c_l = input('Enter number to see that song lyrics: ')
print(arr[int(c_l)])

print('\nTo get more songs of same artist from the list above, choose a number from below:')
c_a = input("0. Love \n 1. Driver \n 2. Mood \n 3. Time \n")



def a_w():
    print('\n-----Weekend-----')
    c_w = input(' 0. Love \n 1. lorem \n 2. lorem\n')
    love = "\nI been tryna call  I been on my own for long enough   Maybe you can show me how to love, maybe I'm going through withdrawals  You don't even have to do too much  You can turn me on with just a touch, baby\n"
    lorem = "\nLorem lorem lorem lorem lorem lorem\n"    
    lorem1 = "\nLorem text is lorem and there is nothing to read in it\n"
    arr_w = [love, lorem, lorem1]
    print(arr_w[int(c_w)])

def a_o():
    print('\n-----Olivia-----')
    c_o = input(' 0. Driver \n 1. Lorem \n 2. Lorem\n')
    driver = "\nI got my drivers license last week,  Just like we always talked about Cause you were so excited for me, To finally drive up to your house\n"
    lorem = "\nLorem lorem lorem lorem lorem lorem\n"    
    lorem1 = "\nLorem text is lorem and there is nothing to read in it\n"
    arr_o = [driver, lorem, lorem1]
    print(arr_o[int(c_o)])

def a_g():
    print('\n-----goldn-----')
    c_g = input(' 0. Mood \n 1. Lorem \n 2. Lorem\n')
    mood = "\nWhy you always in a mood? actin' brand new  I ain't tryna tell you what to do, but try to play it cool  Baby, I ain't playing by your rules  Everything look better with a view\n"
    lorem = "\nLorem lorem lorem lorem lorem lorem\n"    
    lorem1 = "\nLorem text is lorem and there is nothing to read in it\n"
    arr_g = [mood, lorem, lorem1]
    print(arr_o[int(c_g)])

def a_e():
    print('\n-----Ed-----\n')
    c_e = input(' 0. Time \n 1. Lorem \n 2. Lorem\n')
    Time = "\nStop the clocks, it's amazing  You should see the way the light dances off your hair  A million colours of hazel, golden, and red  Saturday morning is fading  The sun's reflected by the coffee in your hand  My eyes are caught in your gaze all over again\n"
    lorem = "\nLorem lorem lorem lorem lorem lorem\n"    
    lorem1 = "\nLorem text is lorem and there is nothing to read in it\n"
    arr_e = [mood, lorem, lorem1]
    print(arr_o[int(c_e)])

if c_a == '0':
    a_w()
elif c_a == '1':
    a_o()
elif c_a == '2':
    a_g()
elif c_a == '3':
    a_e()

