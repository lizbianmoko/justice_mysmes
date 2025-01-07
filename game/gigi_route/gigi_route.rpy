default gigi_route_good_end = ["Good End",
    RouteDay("1st", [
        ChatRoom("League or Not?", "day_1_chatroom_1", '07:00', [gg, ra]),
        ChatRoom("Coffee vs. Tea", "day_1_chatroom_2", '09:00', [cc, ra])]),
    RouteDay('2nd'),
    RouteDay('3rd'),
    RouteDay('4th'),
    RouteDay('5th'),
    RouteDay('6th'),
    RouteDay('7th'),
    RouteDay('8th'),
    RouteDay('9th'),
    RouteDay('10th'),
    RouteDay('Final')]
default gigi_route = Route(
    default_branch=gigi_route_good_end,
    branch_list=None,
    route_history_title="Gigi"
)