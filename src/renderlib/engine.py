import json
import re
from typing import Dict, Any, List, Optional

class MathEngine:
    """गणित के जटिल समीकरणों और सूत्रों को रेंडर करने के लिए इंजन।"""
    def __init__(self):
        self.latex_delimiters = ("$", "$")

    def to_latex(self, expression: str) -> str:
        expression = re.sub(r'(\d+)/(\d+)', r'\\frac{\1}{\2}', expression)
        expression = expression.replace('*', r'\times ')
        return f"{self.latex_delimiters[0]}{expression}{self.latex_delimiters[1]}"

    def render_matrix(self, matrix: List[List[Any]]) -> str:
        rows = [" & ".join(map(str, row)) for row in matrix]
        matrix_body = " \\\\\n  ".join(rows)
        return f"\\begin{{bmatrix}}\n  {matrix_body}\n\\end{{bmatrix}}"

    def render_integral(self, lower: str, upper: str, expression: str, var: str = "x") -> str:
        return f"\\int_{{{lower}}}^{{{upper}}} {expression} \\, d{var}"


class ChemEngine:
    """रासायनिक संरचनाओं, SMILES और समीकरणों को रेंडर करने के लिए इंजन।"""
    def __init__(self):
        pass

    def render_smiles_to_svg(self, smiles_string: str) -> str:
        # Placeholder for RDKit integration: Chem.MolFromSmiles -> Draw.MolsToGridImage
        return f"<svg> </svg>"

    def balance_equation(self, reactants: List[str], products: List[str]) -> str:
        left = " + ".join(reactants)
        right = " + ".join(products)
        return f"{left} \\rightarrow {right}"

    def render_molecule_3d(self, formula: str) -> Dict[str, str]:
        return {"format": "mol/json", "data": f"3D Coordinates for {formula} (Placeholder)"}


class PhysicsEngine:
    """भौतिकी के सर्किट, डायग्राम और क्वांटम मैकेनिक्स समीकरणों के लिए इंजन।"""
    def __init__(self):
        pass

    def render_circuit_svg(self, components: List[Dict[str, Any]]) -> str:
        svg_output = "<svg width='500' height='500'>\n"
        for comp in components:
            svg_output += f"  \n"
        svg_output += "</svg>"
        return svg_output

    def render_bra_ket(self, bra: str, ket: str) -> str:
        return f"\\langle {bra} | {ket} \\rangle"

    def render_vector(self, name: str, components: List[float]) -> str:
        comp_str = ", ".join(map(str, components))
        return f"\\vec{{{name}}} = \\langle {comp_str} \\rangle"


class BiologyEngine:
    """जीव विज्ञान के पाथवे और DNA/RNA अनुक्रमों को रेंडर करने के लिए इंजन।"""
    def __init__(self):
        self.base_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    def render_dna_sequence(self, sequence: str) -> str:
        sequence = sequence.upper()
        complement = "".join([self.base_pairs.get(base, '?') for base in sequence])
        return f"5' - {sequence} - 3'\n     {'|' * len(sequence)}\n3' - {complement} - 5'"

    def render_metabolic_pathway(self, pathway_name: str, enzymes: List[str]) -> str:
        steps = " -> ".join([f"[{enzyme}]" for enzyme in enzymes])
        return f"Pathway: {pathway_name}\nSteps: {steps}"


class EconomicsEngine:
    """अर्थशास्त्र के ग्राफ, सप्लाई-डिमांड कर्व और मैट्रिक्स डेटा के लिए इंजन।"""
    def __init__(self):
        pass

    def render_supply_demand_table(self, price: List[float], supply: List[float], demand: List[float]) -> str:
        table = "| Price ($) | Supply (Qs) | Demand (Qd) |\n"
        table += "|---|---|---|\n"
        for p, s, d in zip(price, supply, demand):
            table += f"| {p} | {s} | {d} |\n"
        return table

    def generate_chart_config(self, title: str, data: Dict[str, List[float]]) -> str:
        config = {
            "title": title,
            "type": "line",
            "data": data
        }
        return json.dumps(config, indent=2)


class MusicEngine:
    """संगीत सिद्धांत, म्यूजिकल स्टाफ और कॉर्ड्स को रेंडर करने के लिए इंजन।"""
    def __init__(self):
        pass

    def render_abc_notation(self, notes: str, meter: str = "4/4", key: str = "C") -> str:
        abc = f"M:{meter}\nK:{key}\n{notes}"
        return f"```abc\n{abc}\n```"

    def render_chord_progression(self, chords: List[str]) -> str:
        return " | ".join(chords) + " |"


class LinguisticsEngine:
    """भाषाविज्ञान (IPA, सिंटैक्स ट्री) के लिए इंजन।"""
    def __init__(self):
        pass

    def format_ipa(self, text: str) -> str:
        return f"/{text}/"

    def render_syntax_tree(self, root: str, branches: List[str]) -> str:
        tree = f"[{root} "
        tree += " ".join([f"[{branch}]" for branch in branches])
        tree += "]"
        return tree


class RenderLib:
    """मुख्य API क्लास जो सभी इंजनों को एक साथ जोड़ती है।"""
    def __init__(self):
        self.math = MathEngine()
        self.chem = ChemEngine()
        self.physics = PhysicsEngine()
        self.biology = BiologyEngine()
        self.economics = EconomicsEngine()
        self.music = MusicEngine()
        self.linguistics = LinguisticsEngine()

    def render(self, subject: str, method: str, *args, **kwargs) -> str:
        try:
            engine = getattr(self, subject.lower())
            func = getattr(engine, method)
            return func(*args, **kwargs)
        except AttributeError:
            return f"Error: '{subject}' engine or '{method}' method not found."

# ---------------------------------------------------------
# उदाहरण उपयोग (Example Usage Data)
# ---------------------------------------------------------
if __name__ == "__main__":
    renderer = RenderLib()
    
    print("--- Math ---")
    print(renderer.math.to_latex("3/4 + x^2 = y"))
    print(renderer.math.render_matrix([[1, 2], [3, 4]]))
    
    print("\n--- Chemistry ---")
    print(renderer.chem.balance_equation(["2H2", "O2"], ["2H2O"]))
    
    print("\n--- Physics ---")
    print(renderer.physics.render_bra_ket("psi", "phi"))
    print(renderer.physics.render_vector("v", [9.81, 0, -1.2]))
    
    print("\n--- Biology ---")
    print(renderer.biology.render_dna_sequence("ATGCGATCG"))
    
    print("\n--- Economics ---")
    print(renderer.economics.render_supply_demand_table([10, 20, 30], [100, 200, 300], [300, 200, 100]))
    
    print("\n--- Music ---")
    print(renderer.music.render_chord_progression(["Cmaj7", "Am7", "Dm7", "G7"]))
    
    print("\n--- Linguistics ---")
    print(renderer.linguistics.format_ipa("həˈloʊ"))
    print(renderer.linguistics.render_syntax_tree("S", ["NP", "VP"]))
