from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(), 
		"players": Player.objects.all(),

		"AFL_teams":League.objects.get(name="American Football League"),
		"SeattleH_Players":Team.objects.get(location="Seattle", team_name="Hurricanes"),
		"AAofBaseball_players":League.objects.get(name="Atlantic Association of Baseball"),
		"NAIH_players":League.objects.get(name="National Association of Ice Hockey"),
		"Sophia":Player.objects.filter(first_name="Sophia"),
		"Coleman":Player.objects.filter(last_name="Coleman"),
		"Ben_Coleman":Player.objects.get(first_name="Benjamin", last_name="Coleman"),
		# Number 10
		"Michigan_Clippers":Team.objects.get(location="Michigan", team_name="Clippers"),

		

		"baseball_leagues": League.objects.filter(sport="Baseball"),
		"womens_leagues": League.objects.filter(name__contains="Womens"),
		"hockey_leagues": League.objects.filter(name__contains="Hockey"),
		"no_football_leagues": League.objects.exclude(sport="Football"),
		"conference_leagues": League.objects.filter(name__contains="Conference"),
		"atlantic_leagues": League.objects.filter(name__startswith="Atlantic"),

		"dallas_teams": Team.objects.filter(location="Dallas"),
		"raptors_teams": Team.objects.filter(team_name__contains="Raptors"),
		"city_teams": Team.objects.filter(location__contains="City"),
		"t_teams": Team.objects.filter(team_name__startswith="T"),
		"rev_team_order": Team.objects.order_by('-team_name'),

		"cooper_players":Player.objects.filter(last_name="Cooper"),
		"joshua_players":Player.objects.filter(first_name="Joshua"),
		"joshua_players":Player.objects.filter(first_name="Joshua"),
		"no_joshua_coopers":Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"alexander_and_wyatt":Player.objects.filter(first_name="Alexander" and "Wyatt"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")