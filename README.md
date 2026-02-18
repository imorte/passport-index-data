# Passport Index Data

Travel visa requirements for 199 countries.

Last updated: **17 February 2026**.

For historical data(<= 2025) check [the repo](https://github.com/ilyankou/passport-index-dataset)

## Files

7 datasets with identical data - one JSON and six CSVs. CSVs come in three country identifier variants: full names, ISO
3166-1 alpha-2 (two-letter), and ISO 3166-1 alpha-3 (three-letter codes).

| File                             | Format               | Country identifiers |
|----------------------------------|----------------------|---------------------|
| `passport-index.json`            | JSON (nested object) | ISO-2               |
| `passport-index-matrix.csv`      | Matrix               | Full country names  |
| `passport-index-matrix-iso2.csv` | Matrix               | ISO-2 codes         |
| `passport-index-matrix-iso3.csv` | Matrix               | ISO-3 codes         |
| `passport-index-tidy.csv`        | Tidy (long)          | Full country names  |
| `passport-index-tidy-iso2.csv`   | Tidy (long)          | ISO-2 codes         |
| `passport-index-tidy-iso3.csv`   | Tidy (long)          | ISO-3 codes         |

**Matrix format** - first column is the passport (origin), each remaining column is a destination.

**Tidy format** - three columns: `Passport` (from), `Destination` (to), `Requirement`.

**JSON format** - nested object keyed by ISO-2 codes: `{ "us": { "gb": { "status": "visa free", "days": 180 }, ... } }`.

## Values

| Value             | Meaning                                                                                                                                                                                                                      |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `7`–`360`         | Number of visa-free days (CSV only; JSON stores `status` and `days` as separate fields)                                                                                                                                      |
| `visa free`       | Visa-free travel where the number of days is unknown or not applicable (e.g. EU freedom of movement). Also covers tourist registration (Seychelles), e-tickets (Dominican Republic), and arrival cards (Singapore, Malaysia) |
| `visa on arrival` | Visa issued upon arrival - effectively visa-free                                                                                                                                                                             |
| `eta`             | Electronic travel authorisation. Includes ESTA (USA), eTA (Canada), eVisitor (Australia), eTourist card (Suriname), and similar schemes                                                                                      |
| `e-visa`          | Electronic visa required                                                                                                                                                                                                     |
| `visa required`   | Standard visa required before travel. Includes Cuba's tourist cards and China's Exit-Entry permits for Macau/Hong Kong                                                                                                       |
| `no admission`    | Entry not permitted (e.g. active travel bans or conflict zones)                                                                                                                                                              |
| `-1`              | Passport country equals destination country                                                                                                                                                                                  |

## Source & License

Data scraped from [passportindex.org](https://www.passportindex.org)
information.

Licensed under [MIT](LICENSE).
