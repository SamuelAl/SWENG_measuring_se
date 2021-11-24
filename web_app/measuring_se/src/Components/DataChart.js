import React from 'react'
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';




export default function DataChart({data}) {
    return (
        <div className="w-11/12" style={{height: "500px"}}>
            <ResponsiveContainer>
                <AreaChart
                    data={data}
                    margin={{
                        top: 10,
                        right: 30,
                        left: 0,
                        bottom: 0,
                    }}
                >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="date" />
                    <YAxis />
                    <Tooltip />
                    <Area type="monotone" dataKey="additions" stackId="1" stroke="#65EB9D" fill="#65EB9D" />
                    <Area type="monotone" dataKey="deletions" stackId="1" stroke="#EB827A" fill="#EB827A" />
                </AreaChart>
            </ResponsiveContainer>

        </div>
    )
}
