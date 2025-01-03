default gigi_route_good_end = ["Good End",
    RouteDay("1st", [
        ChatRoom("Justice Just Like That", "day_1_chatroom_2", '07:00', [gg, ra])]),
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