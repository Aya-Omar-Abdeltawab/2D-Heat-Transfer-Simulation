import plotly.graph_objects as go

class HeatMapVisualizer:
    @staticmethod
    def create_animation(frames):
        fig = go.Figure()

        fig.add_trace(
            go.Heatmap(
                z=frames[0],
                colorscale='hot',
                showscale=True,
                colorbar=dict(title='Temperature')
            )
        )

        fig.frames = [
            go.Frame(
                data=[go.Heatmap(z=frame)],
                name=f'frame{i}'
            )
            for i, frame in enumerate(frames)
        ]

        fig.update_layout(
            title="Heat Transfer Simulation",
            xaxis=dict(title="X Position"),
            yaxis=dict(title="Y Position", scaleanchor="x", scaleratio=1),
            updatemenus=[{
                'buttons': [
                    {
                        'args': [None, {'frame': {'duration': 50, 'redraw': True},
                                      'fromcurrent': True}],
                        'label': 'Play',
                        'method': 'animate'
                    },
                    {
                        'args': [[None], {'frame': {'duration': 0, 'redraw': True},
                                        'mode': 'immediate',
                                        'transition': {'duration': 0}}],
                        'label': 'Pause',
                        'method': 'animate'
                    }
                ],
                'type': 'buttons',
                'showactive': False,
                'x': 0.1,
                'y': 1.1,
                'xanchor': 'right',
                'yanchor': 'top'
            }],
            sliders=[{
                'currentvalue': {'prefix': 'Step: '},
                'steps': [
                    {
                        'args': [[f'frame{k}'],
                                {'frame': {'duration': 0, 'redraw': True},
                                 'mode': 'immediate'}],
                        'label': str(k),
                        'method': 'animate'
                    }
                    for k in range(len(frames))
                ]
            }]
        )

        return fig
