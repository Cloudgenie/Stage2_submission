def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

my_new_notes = [ ['Variables', 'Values are assigned to variables'],
                  ['Functions', 'Functions reduce repetitive code and can be re-used'],
                	 ['Decisions', 'The "if" statement allows control of the flow of execution of your code'],
                        ['Lists', 'Data can be stored in lists and be processed'] ]


def make_HTML_for_many_concepts(concepts_list):
    HTML = ""
    for concept in concepts_list:
        new_HTML = make_HTML(concept)
        HTML = HTML + new_HTML
    return HTML

print make_HTML_for_many_concepts(my_new_notes)
