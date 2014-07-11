import nose 

from hlt.corpus import icle 

def test_icle():












def test_promptAdherence	
	raw = prompta.essays
	lemm = icle.lemmatized
	ann = icle.annotized

	raw['BGSU1037'].prompt.raw()
	raw['BGSU1037'].response

	lemm['BGSU1037'].prompt
	lemm['BGSU1037'].response

				#[Annotater][Claim]
	ann['BGSU1037'][0][0].claim 
	ann['BGSU1037'][0][0].claim 
	ann['BGSU1037'][0][0].agreement
	ann['BGSU1037'][0][0].confidence
	ann['BGSU1037'][0][0].reasons
	ann['BGSU1037'][0][0].rationale

	icle['BGSU1037'].essay.prompt
	agreement = [ claim.agreement for claim in icle['BGSU1037'].annotation[0] ]