# Governança e valor público em acordos de cooperação técnica federais – dados e códigos

Material suplementar do artigo **"Governança e valor público em acordos de cooperação técnica federais"**, submetido à *Revista de Administração Pública* (RAP/FGV).

## Conteúdo

| Pasta | Arquivo | Descrição |
|---|---|---|
| `dados/` | `matriz_codificacao_act_2025.csv` | Escores (0–3) dos 61 ACTs nos 22 indicadores, somas D1–D5 e cluster atribuído |
| `dados/` | `evidencias_textuais.csv` | Trechos literais das cláusulas que fundamentam cada escore |
| `dados/` | `dicionario_de_dados.csv` | Descrição de cada variável |
| `protocolo/` | `protocolo_codificacao.pdf` | Definição dos indicadores e regras da escala 0–3 |
| `codigo/` | `analise_clusters.py` | Padronização (escore z), seleção de k (cotovelo e silhueta, k = 2 a 9) e k-means (k = 4) |

## Fonte dos documentos analisados

Brasil. Ministério da Gestão e da Inovação em Serviços Públicos. (2025). *Acordos de cooperação técnica – 2025*.
https://www.gov.br/gestao/pt-br/acesso-a-informacao/acordos-de-cooperacao-tecnica/2025 (consulta em 22 jan. 2026).

## Escala de codificação

0 = ausente; 1 = menção genérica; 2 = previsão explícita; 3 = previsão detalhada e operacionalizada.
A ausência de evidência textual explícita foi codificada como 0. O ACT 72/2025, publicado apenas como extrato, foi mantido no corpus.

## Reprodução da análise

```bash
pip install pandas numpy scikit-learn matplotlib
python codigo/analise_clusters.py
```

Parâmetros: StandardScaler; KMeans com distância euclidiana, `random_state = 42`, `n_init = 100`; silhueta média da solução k = 4 ≈ 0,38.

## Licença

Dados e documentação: CC BY 4.0. Código: MIT.

## Como citar

Ver `CITATION.cff` ou o registro no Zenodo (DOI: 10.5281/zenodo.23002818).
