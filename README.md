# Investment Sentiment Analysis

AI-powered analysis of investment market sentiment from X/Twitter posts, built with LangGraph, MCP tools, and the X API.

## Project Description

This repository contains an AI-driven investment research system that analyzes market sentiment by collecting and processing X/Twitter posts related to key investment themes. The system uses advanced AI capabilities to identify trends, sentiment patterns, and emerging narratives in the investment landscape.

The analysis focuses on real-time social media sentiment to provide insights into:
- Institutional adoption trends
- Market momentum indicators
- Emerging investment themes
- Regulatory sentiment shifts
- Corporate strategy developments

## Topics Analyzed

### Primary Investment Areas
- **Bitcoin & Cryptocurrency Institutional Adoption**
  - Corporate treasury strategies (MicroStrategy, Metaplanet)
  - ETF market expansion and regulatory developments
  - Cross-asset institutional recognition
  - Bitcoin as reserve currency alternative

- **Reinsurance Market Trends**
  - Technology transformation in reinsurance
  - Capital efficiency improvements
  - Market evolution drivers

- **Stone Ridge Asset Management**
  - Company developments and market positioning
  - Strategic initiatives and market commentary

### Key Metrics Tracked
- Sentiment polarity (positive/negative/neutral)
- Engagement metrics (likes, retweets, comments)
- Theme frequency and trending topics
- Institutional player mentions
- Price correlation indicators

## How It Was Built

### Architecture Overview
This project leverages a sophisticated AI agent architecture powered by:

- **LangGraph Agent**: Orchestrates the entire analysis workflow, managing data collection, processing, and report generation
- **Claude Sonnet**: Provides advanced natural language processing and sentiment analysis capabilities
- **GitHub MCP (Model Context Protocol) Tools**: Handles repository operations including file creation, branch management, and pull request workflows
- **X API v2**: Retrieves real-time social media posts for analysis

### Technology Stack
- **AI/ML**: Claude Sonnet for natural language understanding and sentiment analysis
- **Workflow Orchestration**: LangGraph for agent-based task management
- **Data Collection**: X API v2 for social media post retrieval
- **Repository Management**: GitHub MCP tools for automated Git operations
- **Data Processing**: Python for data manipulation and analysis
- **Output Format**: Structured Markdown reports and JSON metadata

### Key Components
1. **Data Collection Agent**: Searches X/Twitter using targeted queries
2. **Sentiment Analysis Engine**: Processes posts for sentiment and theme extraction
3. **Report Generation System**: Creates structured markdown summaries
4. **Repository Management**: Automated Git operations for version control
5. **Metadata Tracking**: Comprehensive analysis parameter documentation

## Repository Contents

- `summary.md` - Comprehensive market sentiment analysis report
- `metadata.json` - Analysis parameters, themes, and metrics
- `x_search.py` - Python script for X API post retrieval
- `README.md` - Project documentation (this file)

## Replicating the Process

### Prerequisites
1. **X API Access**: Obtain X API v2 Bearer Token
2. **Claude API Access**: Access to Claude Sonnet model
3. **GitHub Access**: Repository permissions for MCP operations
4. **Python Environment**: Python 3.8+ with required packages

### Setup Instructions

#### 1. Environment Configuration
```bash
# Set up environment variables
export X_BEARER_TOKEN="your_x_api_bearer_token"
export ANTHROPIC_API_KEY="your_claude_api_key"
export GITHUB_TOKEN="your_github_token"
```

#### 2. Install Dependencies
```bash
pip install requests anthropic langgraph
```

#### 3. Configure LangGraph Agent
Set up the LangGraph agent with:
- X API tools for post retrieval
- GitHub MCP tools for repository operations
- Claude Sonnet for sentiment analysis

#### 4. Run Analysis
```python
# Example search queries
queries = [
    "bitcoin institutional adoption",
    "reinsurance market trends", 
    "Stone Ridge",
    "MicroStrategy bitcoin",
    "bitcoin ETF"
]

# Execute analysis workflow
for query in queries:
    posts = search_recent_posts(query, max_results=20)
    sentiment_data = analyze_sentiment(posts)
    themes = extract_themes(sentiment_data)
```

#### 5. Generate Reports
The system automatically:
- Creates structured markdown reports
- Generates JSON metadata files
- Manages Git operations (branches, commits, PRs)
- Tracks analysis parameters and results

### Customization Options

#### Search Parameters
- Modify search queries in `metadata.json`
- Adjust date ranges for historical analysis
- Configure post volume limits

#### Analysis Focus
- Add new investment themes
- Customize sentiment scoring
- Modify engagement weight factors

#### Output Format
- Customize markdown report structure
- Add new metadata fields
- Configure automated reporting schedules

## Analysis Methodology

### Data Collection
1. **Query Design**: Targeted searches for investment-related content
2. **Temporal Scope**: Recent posts (last 7 days) for current sentiment
3. **Volume Control**: Balanced sample sizes across themes
4. **Quality Filtering**: Engagement-based relevance scoring

### Sentiment Processing
1. **Theme Extraction**: AI-powered identification of investment themes
2. **Sentiment Classification**: Multi-dimensional sentiment analysis
3. **Engagement Weighting**: Popularity-adjusted sentiment scoring
4. **Trend Identification**: Temporal sentiment pattern analysis

### Report Generation
1. **Structured Analysis**: Organized by themes and metrics
2. **Statistical Summary**: Quantitative sentiment indicators
3. **Notable Content**: High-engagement post highlighting
4. **Metadata Documentation**: Complete analysis parameter tracking

## Future Enhancements

- **Real-time Monitoring**: Continuous sentiment tracking
- **Predictive Analytics**: Sentiment-based market prediction models
- **Multi-platform Integration**: Expand beyond X to other social platforms
- **Automated Alerts**: Threshold-based sentiment change notifications
- **Historical Analysis**: Long-term sentiment trend analysis
- **Portfolio Integration**: Connect sentiment data to investment strategies

## Contributing

This project demonstrates AI-powered investment research capabilities. Contributions welcome for:
- Additional data sources
- Enhanced sentiment models
- New analysis themes
- Improved visualization
- Extended automation features

---

*Generated using AI-powered investment sentiment analysis - combining social media intelligence with advanced natural language processing for market insights.*