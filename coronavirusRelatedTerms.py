#LIST OF TERMS RELATED TO CORONAVIRUS

#HIGH CORRELATION: basically synonims; we can assume that a post
#containing one of this worlds is talking about covid-19
coronavirus_terms_high_corr = [
	'coronavirus',
	'corona',
	'virus',
	'covid',
	'covid19',
	'covid-19',
	'flu',
	'wuhan',
	'Coronaviridae',
	'N95'
]

#MEDIUM CORRELATION: worlds that have been widely used together with 
#'Coronavirus' in the last few months, but are normally used as well.
#We can assume that a post from March/April 2020 containing one of these
#words is very likely talking about Coronavirus
coronavirus_terms_medium_corr = [
	'symptoms',
	'cases',
	'helpers',
	'death',
	'deaths',
	'test',
	'mask',
	'masks',
	'disinfectant',
	'lombardy',
	'infection',
	'vaccine',
	'pandemic',
	'cdc',
	'outbreak'
]

#LOW CORRELATION: worlds widely used with 'Coronavirus', which however
#are used in unrelated posts as well, even in this period. A post that
#contains only one of these words, and none from before,
#has a high chance of being unrelated
coronavirus_terms_low_corr = [
	'updates',
	'update',
	'latest',
	'news',
	'tips',
	'statistics',
	'wet',
	'market',
	'bats',
	'who',
	'ccp',
	'china',
	'chinese'
]
