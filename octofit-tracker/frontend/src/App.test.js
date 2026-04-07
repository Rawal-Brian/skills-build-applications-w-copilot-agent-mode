import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import App from './App';

test('renders OctoFit Tracker app', () => {
  render(
    <BrowserRouter>
      <App />
    </BrowserRouter>
  );
  const headerElement = screen.getByText(/OctoFit Tracker/i);
  expect(headerElement).toBeInTheDocument();
});
