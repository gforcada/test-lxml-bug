# -*- coding: utf-8 -*-
try:
    from cStringIO import StringIO
    PY = 2
except ModuleNotFoundError:
    from io import StringIO
    PY = 3
from lxml import etree
from lxml.html import HTMLParser

import os

def get_transform(filename):
    xsl_path = os.path.join(os.path.dirname(__file__), filename)
    cleanup_html_xslt = os.path.abspath(xsl_path)
    styletree = etree.parse(cleanup_html_xslt)
    return etree.XSLT(styletree)


def test_weird_behavior():
    original = u"""<p>Drei AfD-Abgeordnete haben „Gäste“ ins Gebäude des Bundestags geholt, die dort Abgeordnete und den Bundeswirtschaftsminister Peter Altmaier belästigten. Hinterher entschuldigten sich die Fraktionsvorsitzenden Alice Weidel und Alexander Gauland, aber das war nicht überzeugend, weil man die Guerillataktik ihrer Partei – erst skandalöse Vorstöße, dann Rückzüge – seit Langem kennt. So versucht sie immer wieder, das Parlament und die Demokratie als Ganzes zu diskreditieren. Vonseiten der AfD wird auch gestreut, solche kleinen Regelwidrigkeiten habe es doch schon immer gegeben. Das stimmt nicht. Regelwidrigkeit ist nicht gleich Regelwidrigkeit: In diesem Fall hat die AfD eine rote Linie überschritten. Sie hat versucht, frei gewählte Abgeordnete bei der Ausübung ihres Mandats unter Druck zu setzen.</p><p>Nehmen wir die beiden Plakataktionen, die es gegeben hat, eine vonseiten der AfD, die andere von der Linkspartei. AfD-Abgeordnete hoben am Mittwoch voriger Woche Plakate mit Trauerflor in die Höhe, auf denen „Grundgesetz 18. 11. 2020“ stand, während Bundesgesundheitsminister Jens Spahn seine Rede hielt. Das war ein klarer Verstoß gegen die Hausordnung, die jegliche Form des Demonstrierens verbietet. Schon das Tragen gewisser Kleidungsstücke kann als unerlaubte Störung gelten, und Besucher auf der Empore dürfen nicht in den Saal hineinrufen, geschweige denn in den Fluren Abgeordnete verfolgen. Die Plakataktion der Linkspartei im Jahr 2010 richtete sich gegen die Militärpräsenz in Afghanistan. Die Opfer des Luftangriffs bei Kundus waren namentlich auf den Plakaten verzeichnet. In beiden Fällen wurden die Abgeordneten vom Präsidium aus aufgefordert, die Aktion sofort zu beenden. Die AfD kam der Aufforderung nach, die Linkspartei zögerte; als ihre Plakatträger des Saales verwiesen wurden, folgte ihnen die ganze Fraktion.</p><h2>Auf Durchzug geschaltet</h2><p>Hier nur zwei Ausgestaltungen derselben politischen Taktik zu sehen, wäre falsch. Nein, die Linke nimmt das Parlament ernst und will in ihm Gehör finden, während die AfD den Parlamentarismus infrage stellt. Das erschließt sich aber nicht aus dem bloßen Vergleich der beiden Aktionen. Man muss vielmehr wissen, dass das Grundgesetz mit Trauerflor auf die Behauptung der AfD anspielt, die Bundesregierung verschaffe sich ein „Ermächtigungsgesetz“ wie Adolf Hitler 1933. Doch wir wollen diesen Kontext zunächst ausblenden. Dann erscheinen die Plakate der AfD als bloße Ordnungswidrigkeit. Ob die Neufassung des Infektionsschutzgesetzes in allem grundgesetzkonform ist, wird ja auch von Linken bezweifelt. Der Protest in Form von Plakaten würde sich daraus erklären, dass AfD wie Linkspartei ihre „Ausgrenzung“ durch die anderen Fraktionen beklagen.</p><p>Zwar wurde die Aktion der Linkspartei von Thomas Oppermann, dem damaligen Parlamentarischen Geschäftsführer der SPD-Fraktion, mit den Worten gerügt, im Parlament zähle „das Argument, nicht das Transparent“, denn es sei „Ort der Debatte, nicht der Demonstration“; aber er verschwieg, was jedermann wusste, dass nämlich die SPD auf Durchzug schaltete, sobald Abgeordnete der Linken zu argumentieren begannen. Eben deshalb gerierte sich diese Fraktion als außerparlamentarische Opposition: Wenn die anderen meinten, sie sei im Bundestag fehl am Platz, so spiegelte sie das zurück.</p><p>Ordnungswidrigkeiten hat es viele gegeben, und nicht selten bringt man Sympathie für sie auf. Etwa wenn Joschka Fischer Turnschuhe trug, als er im hessischen Parlament zum Minister vereidigt wurde. Das war Protest mit klar erkennbarem Inhalt: Für Seriosität ist noch so korrekte Kleidung kein Beleg. Dass er einmal ausrief, in der Frühphase seiner grünen Partei, „mit Verlaub, Herr Präsident, Sie sind ein Arschloch“, lässt man dann auch noch durchgehen. All das tangiert keine rote Linie. Auch die Flugblattaktion von Extinction Rebellion in der Lobby des Bundestags, Juli 2020, hat es nicht getan. Wohl aber wurde sie überschritten, als 2014 drei Abgeordnete der Linkspartei „Gäste“ einluden, von denen Gregor Gysi bedrängt und bis zur Toilette verfolgt wurde.</p>"""
    html = original.encode('ascii', 'xmlcharrefreplace')
    if PY == 3:
        html = html.decode('utf-8')
    parser = HTMLParser(recover=True, remove_blank_text=True, remove_comments=True)
    htmltree = etree.parse(StringIO(html), parser)
    resulttree = get_transform('article.xsl')(htmltree)
    cleaned_html = etree.tostring(resulttree)
    if PY ==3:
        assert b'von denen Gregor Gysi' in cleaned_html
    else:
        assert 'von denen Gregor Gysi' in cleaned_html
