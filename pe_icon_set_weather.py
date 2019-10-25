#! python3

_names = {
    'pe-is-w-blizzard'                    :  '\ue901',
    'pe-is-w-cloud-down'                  :  '\ue903',
    'pe-is-w-cloud-refresh'               :  '\ue905',
    'pe-is-w-cloud-up'                    :  '\ue907',
    'pe-is-w-compass-e'                   :  '\ue909',
    'pe-is-w-compass-n'                   :  '\ue90c',
    'pe-is-w-compass-s'                   :  '\ue90e',
    'pe-is-w-compass-w'                   :  '\ue910',
    'pe-is-w-compass'                     :  '\ue911',
    'pe-is-w-degree-celsius'              :  '\ue912',
    'pe-is-w-degree-fahrenheit'           :  '\ue913',
    'pe-is-w-drizzle'                     :  '\ue915',
    'pe-is-w-drop-cloud'                  :  '\ue917',
    'pe-is-w-drop-percentage'             :  '\ue91a',
    'pe-is-w-drop'                        :  '\ue91b',
    'pe-is-w-drops'                       :  '\ue91d',
    'pe-is-w-eclipse-1'                   :  '\ue91f',
    'pe-is-w-eclipse-2'                   :  '\ue921',
    'pe-is-w-eclipse-3'                   :  '\ue923',
    'pe-is-w-eclipse-4'                   :  '\ue925',
    'pe-is-w-fog-1'                       :  '\ue927',
    'pe-is-w-fog-2'                       :  '\ue929',
    'pe-is-w-fog-3'                       :  '\ue92b',
    'pe-is-w-fog-4'                       :  '\ue92d',
    'pe-is-w-full-moon-1'                 :  '\ue92f',
    'pe-is-w-full-moon-2'                 :  '\ue931',
    'pe-is-w-full-moon-3'                 :  '\ue933',
    'pe-is-w-hail-1'                      :  '\ue935',
    'pe-is-w-hail-2'                      :  '\ue937',
    'pe-is-w-hail-day-1'                  :  '\ue939',
    'pe-is-w-hail-day-2'                  :  '\ue93b',
    'pe-is-w-hail-full-moon-1'            :  '\ue93d',
    'pe-is-w-hail-full-moon-2'            :  '\ue93f',
    'pe-is-w-hail-night-1'                :  '\ue941',
    'pe-is-w-hail-night-2'                :  '\ue943',
    'pe-is-w-heavy-hail-day'              :  '\ue945',
    'pe-is-w-heavy-hail-full-moon'        :  '\ue948',
    'pe-is-w-heavy-hail-night'            :  '\ue94a',
    'pe-is-w-heavy-hail'                  :  '\ue94b',
    'pe-is-w-heavy-rain-1'                :  '\ue94d',
    'pe-is-w-heavy-rain-2'                :  '\ue94f',
    'pe-is-w-heavy-rain-day'              :  '\ue951',
    'pe-is-w-heavy-rain-full-moon'        :  '\ue953',
    'pe-is-w-heavy-rain-night'            :  '\ue955',
    'pe-is-w-mist'                        :  '\ue956',
    'pe-is-w-mix-rainfall-1'              :  '\ue958',
    'pe-is-w-mix-rainfall-2'              :  '\ue95a',
    'pe-is-w-moon-1'                      :  '\ue95c',
    'pe-is-w-moon-2'                      :  '\ue95e',
    'pe-is-w-moon-3'                      :  '\ue960',
    'pe-is-w-moon-4'                      :  '\ue962',
    'pe-is-w-moon-horizon'                :  '\ue965',
    'pe-is-w-moon-sea'                    :  '\ue968',
    'pe-is-w-mostly-cloudy-1'             :  '\ue96e',
    'pe-is-w-mostly-cloudy-2'             :  '\ue970',
    'pe-is-w-partly-cloudy-1'             :  '\ue972',
    'pe-is-w-partly-cloudy-2'             :  '\ue974',
    'pe-is-w-partly-cloudy-3'             :  '\ue976',
    'pe-is-w-rain-1'                      :  '\ue978',
    'pe-is-w-rain-and-snow'               :  '\ue97a',
    'pe-is-w-rain-day'                    :  '\ue97c',
    'pe-is-w-rain-full-moon'              :  '\ue97e',
    'pe-is-w-rain-night'                  :  '\ue980',
    'pe-is-w-severe-thunderstorm'         :  '\ue982',
    'pe-is-w-snow-day-1'                  :  '\ue984',
    'pe-is-w-snow-day-2'                  :  '\ue986',
    'pe-is-w-snow-day-3'                  :  '\ue988',
    'pe-is-w-snow-full-moon-1'            :  '\ue98b',
    'pe-is-w-snow-full-moon-2'            :  '\ue98d',
    'pe-is-w-snow-full-moon-3'            :  '\ue98f',
    'pe-is-w-snow-night-1'                :  '\ue991',
    'pe-is-w-snow-night-2'                :  '\ue993',
    'pe-is-w-snow-night-3'                :  '\ue995',
    'pe-is-w-snow'                        :  '\ue996',
    'pe-is-w-snowflake'                   :  '\ue997',
    'pe-is-w-sun-1'                       :  '\ue999',
    'pe-is-w-sun-2'                       :  '\ue99b',
    'pe-is-w-sun-horizon-1'               :  '\ue99d',
    'pe-is-w-sun-horizon-2'               :  '\ue99f',
    'pe-is-w-sunrise'                     :  '\ue9a1',
    'pe-is-w-sunset'                      :  '\ue9a3',
    'pe-is-w-thermometer-1'               :  '\ue9a5',
    'pe-is-w-thermometer-2'               :  '\ue9a7',
    'pe-is-w-thermometer-3'               :  '\ue9a9',
    'pe-is-w-thermometer-4'               :  '\ue9ab',
    'pe-is-w-thermometer-5'               :  '\ue9ad',
    'pe-is-w-thunderbolt-1'               :  '\ue9af',
    'pe-is-w-thunderbolt-2'               :  '\ue9b1',
    'pe-is-w-thunderstorm-day-1'          :  '\ue9b3',
    'pe-is-w-thunderstorm-day-2'          :  '\ue9b5',
    'pe-is-w-thunderstorm-full-moon-1'    :  '\ue9b8',
    'pe-is-w-thunderstorm-full-moon-2'    :  '\ue9ba',
    'pe-is-w-thunderstorm-night-1'        :  '\ue9bc',
    'pe-is-w-thunderstorm-night-2'        :  '\ue9be',
    'pe-is-w-thunderstorm'                :  '\ue9bf',
    'pe-is-w-tornado-1'                   :  '\ue9c0',
    'pe-is-w-tornado-2'                   :  '\ue9c1',
    'pe-is-w-umbrella'                    :  '\ue9c3',
    'pe-is-w-wind-2'                      :  '\ue9c4',
    'pe-is-w-wind-cloud'                  :  '\ue9c5',
    'pe-is-w-wind-cone'                   :  '\ue9c7',
    'pe-is-w-wind-day'                    :  '\ue9c8',
    'pe-is-w-wind-full-moon'              :  '\ue9c9',
    'pe-is-w-wind-moon'                   :  '\ue9ca',
    'pe-is-w-wind-night'                  :  '\ue9cb',
    'pe-is-w-wind-sun'                    :  '\ue9cc',
    'pe-is-w-wind-turbine'                :  '\ue9ce',
    'pe-is-w-wind'                        :  '\ue9cf',
    'pe-is-w-blizzard-f'                  :  '\ue900',
    'pe-is-w-cloud-down-f'                :  '\ue902',
    'pe-is-w-cloud-refresh-f'             :  '\ue904',
    'pe-is-w-cloud-up-f'                  :  '\ue906',
    'pe-is-w-compass-e-f'                 :  '\ue908',
    'pe-is-w-compass-f'                   :  '\ue90a',
    'pe-is-w-compass-n-f'                 :  '\ue90b',
    'pe-is-w-compass-s-f'                 :  '\ue90d',
    'pe-is-w-compass-w-f'                 :  '\ue90f',
    'pe-is-w-drizzle-f'                   :  '\ue914',
    'pe-is-w-drop-cloud-f'                :  '\ue916',
    'pe-is-w-drop-f'                      :  '\ue918',
    'pe-is-w-drop-percentage-f'           :  '\ue919',
    'pe-is-w-drops-f'                     :  '\ue91c',
    'pe-is-w-eclipse-1-f'                 :  '\ue91e',
    'pe-is-w-eclipse-2-f'                 :  '\ue920',
    'pe-is-w-eclipse-3-f'                 :  '\ue922',
    'pe-is-w-eclipse-4-f'                 :  '\ue924',
    'pe-is-w-fog-1-f'                     :  '\ue926',
    'pe-is-w-fog-2-f'                     :  '\ue928',
    'pe-is-w-fog-3-f'                     :  '\ue92a',
    'pe-is-w-fog-4-f'                     :  '\ue92c',
    'pe-is-w-full-moon-1-f'               :  '\ue92e',
    'pe-is-w-full-moon-2-f'               :  '\ue930',
    'pe-is-w-full-moon-3-f'               :  '\ue932',
    'pe-is-w-hail-1-f'                    :  '\ue934',
    'pe-is-w-hail-2-f'                    :  '\ue936',
    'pe-is-w-hail-day-1-f'                :  '\ue938',
    'pe-is-w-hail-day-2-f'                :  '\ue93a',
    'pe-is-w-hail-full-moon-1-f'          :  '\ue93c',
    'pe-is-w-hail-full-moon-2-f'          :  '\ue93e',
    'pe-is-w-hail-night-1-f'              :  '\ue940',
    'pe-is-w-hail-night-2-f'              :  '\ue942',
    'pe-is-w-heavy-hail-day-f'            :  '\ue944',
    'pe-is-w-heavy-hail-f'                :  '\ue946',
    'pe-is-w-heavy-hail-full-moon-f'      :  '\ue947',
    'pe-is-w-heavy-hail-night-f'          :  '\ue949',
    'pe-is-w-heavy-rain-1-f'              :  '\ue94c',
    'pe-is-w-heavy-rain-2-f'              :  '\ue94e',
    'pe-is-w-heavy-rain-day-f'            :  '\ue950',
    'pe-is-w-heavy-rain-full-moon-f'      :  '\ue952',
    'pe-is-w-heavy-rain-night-f'          :  '\ue954',
    'pe-is-w-mix-rainfall-1-f'            :  '\ue957',
    'pe-is-w-mix-rainfall-2-f'            :  '\ue959',
    'pe-is-w-moon-1-f'                    :  '\ue95b',
    'pe-is-w-moon-2-f'                    :  '\ue95d',
    'pe-is-w-moon-3-f'                    :  '\ue95f',
    'pe-is-w-moon-4-f'                    :  '\ue961',
    'pe-is-w-moon-first-quarter-f'        :  '\ue963',
    'pe-is-w-moon-horizon-f'              :  '\ue964',
    'pe-is-w-moon-last-quarter-f'         :  '\ue966',
    'pe-is-w-moon-sea-f'                  :  '\ue967',
    'pe-is-w-moon-waning-crescent-f'      :  '\ue969',
    'pe-is-w-moon-waning-gibbous-f'       :  '\ue96a',
    'pe-is-w-moon-waxing-crescent-f'      :  '\ue96b',
    'pe-is-w-moon-waxing-gibbous-f'       :  '\ue96c',
    'pe-is-w-mostly-cloudy-1-f'           :  '\ue96d',
    'pe-is-w-mostly-cloudy-2-f'           :  '\ue96f',
    'pe-is-w-partly-cloudy-1-f'           :  '\ue971',
    'pe-is-w-partly-cloudy-2-f'           :  '\ue973',
    'pe-is-w-partly-cloudy-3-f'           :  '\ue975',
    'pe-is-w-rain-1-f'                    :  '\ue977',
    'pe-is-w-rain-and-snow-f'             :  '\ue979',
    'pe-is-w-rain-day-f'                  :  '\ue97b',
    'pe-is-w-rain-full-moon-f'            :  '\ue97d',
    'pe-is-w-rain-night-f'                :  '\ue97f',
    'pe-is-w-severe-thunderstorm-f'       :  '\ue981',
    'pe-is-w-snow-day-1-f'                :  '\ue983',
    'pe-is-w-snow-day-2-f'                :  '\ue985',
    'pe-is-w-snow-day-3-f'                :  '\ue987',
    'pe-is-w-snow-f'                      :  '\ue989',
    'pe-is-w-snow-full-moon-1-f'          :  '\ue98a',
    'pe-is-w-snow-full-moon-2-f'          :  '\ue98c',
    'pe-is-w-snow-full-moon-3-f'          :  '\ue98e',
    'pe-is-w-snow-night-1-f'              :  '\ue990',
    'pe-is-w-snow-night-2-f'              :  '\ue992',
    'pe-is-w-snow-night-3-f'              :  '\ue994',
    'pe-is-w-sun-1-f'                     :  '\ue998',
    'pe-is-w-sun-2-f'                     :  '\ue99a',
    'pe-is-w-sun-horizon-1-f'             :  '\ue99c',
    'pe-is-w-sun-horizon-2-f'             :  '\ue99e',
    'pe-is-w-sunrise-f'                   :  '\ue9a0',
    'pe-is-w-sunset-f'                    :  '\ue9a2',
    'pe-is-w-thermometer-1-f'             :  '\ue9a4',
    'pe-is-w-thermometer-2-f'             :  '\ue9a6',
    'pe-is-w-thermometer-3-f'             :  '\ue9a8',
    'pe-is-w-thermometer-4-f'             :  '\ue9aa',
    'pe-is-w-thermometer-5-f'             :  '\ue9ac',
    'pe-is-w-thunderbolt-1-f'             :  '\ue9ae',
    'pe-is-w-thunderbolt-2-f'             :  '\ue9b0',
    'pe-is-w-thunderstorm-day-1-f'        :  '\ue9b2',
    'pe-is-w-thunderstorm-day-2-f'        :  '\ue9b4',
    'pe-is-w-thunderstorm-f'              :  '\ue9b6',
    'pe-is-w-thunderstorm-full-moon-1-f'  :  '\ue9b7',
    'pe-is-w-thunderstorm-full-moon-2-f'  :  '\ue9b9',
    'pe-is-w-thunderstorm-night-1-f'      :  '\ue9bb',
    'pe-is-w-thunderstorm-night-2-f'      :  '\ue9bd',
    'pe-is-w-umbrella-f'                  :  '\ue9c2',
    'pe-is-w-wind-cone-f'                 :  '\ue9c6',
    'pe-is-w-wind-turbine-f'              :  '\ue9cd',
}

def lookup(data):
    if isinstance(data, str):
        data = [ data ]
    v = ''.join(_names[n] for n in data)
    return v

def name(char):
    for k, v in _names.items():
        if v == char:
            return k
    return None

charset = _names.values()

if __name__ == '__main__':
    text = ''.join(charset)
    print(text)
