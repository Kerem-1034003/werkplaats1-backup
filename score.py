import json

def load_json_data(score_file):
    with open(score_file) as scores_file:
        data = json.load(scores_file)
    return data


def update_scores(score, json_data):
    if score > 0:
        new_player_score = {'amount': score}
        json_data['scores'].append(new_player_score)
        with open('scores.json', 'w') as f:
            json.dump(json_data, f, indent=2)
    
        print(f'Score has been updated: {score}')
    else:
        print(f'Score was {score}, so it has not been updated!')


def get_high_score(data):
    high_score = 0
    for score in data['scores']:
        if score['amount'] > high_score:
            high_score = score['amount']
            return high_score